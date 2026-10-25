from contextlib import asynccontextmanager
import asyncio
import json
from typing import Literal
from uuid import uuid4

import redis.asyncio as redis
from fastapi import FastAPI, HTTPException, Request, status
from pydantic import BaseModel, Field

# 本地 Docker Redis 映射到宿主机 6380 端口；db0 用于学习实验。
# 6379 已被本机其他 Redis 占用，避免实验 API 误连到错误实例。
REDIS_URL = "redis://localhost:6380/0"


class CacheWriteDTO(BaseModel):
    """写入通用缓存的请求体。"""

    value: str = Field(min_length=1, max_length=500)
    ttl_seconds: int = Field(default=60, ge=1, le=3600)


class CacheReadDTO(BaseModel):
    """读取通用缓存的响应体。"""

    key: str
    value: str
    ttl_seconds: int


class ProductReadDTO(BaseModel):
    """商品详情；cache 字段用来观察命中还是回源。"""

    id: int
    name: str
    price: int
    cache: Literal["hit", "miss"]


class ProductUpdateDTO(BaseModel):
    """商品局部更新；只传要改的字段。"""

    name: str | None = Field(default=None, min_length=1, max_length=100)
    price: int | None = Field(default=None, gt=0)


# 用内存字典模拟「主库 / 数据源」，方便观察回源次数
products: dict[int, dict[str, int | str]] = {
    42: {"id": 42, "name": "Keyboard", "price": 99},
}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 应用启动时建连，挂到 app.state，请求里直接复用
    client = redis.from_url(REDIS_URL, decode_responses=True)
    await client.ping()
    app.state.redis = client

    try:
        yield
    finally:
        # 应用关闭时断开连接，避免连接泄漏
        await client.aclose()


app = FastAPI(
    title="Redis Learning Lab",
    description="A minimal FastAPI application for Redis experiments.",
    lifespan=lifespan,
)


def cache_key(key: str) -> str:
    """通用缓存 key，加前缀避免和其他实验撞名。"""
    return f"lab:cache:{key}"


def product_cache_key(product_id: int) -> str:
    """
    商品详情缓存 key。
    末尾 v1：结构变更时可换版本，旧 key 自然失效。
    """
    return f"cache:product:{product_id}:detail:v1"


def rebuild_lock_key(product_id: int) -> str:
    return f"lock:cache:product:{product_id}:detail:v1"


def product_not_found_error() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={"code": "PRODUCT_NOT_FOUND", "message": "Product was not found"},
    )


async def cached_product_or_none(
    client: redis.Redis,
    redis_key: str,
) -> ProductReadDTO | None:
    cached_product = await client.get(redis_key)

    if cached_product == NOT_FOUND_SENTINEL:
        raise product_not_found_error()
    if cached_product is None:
        return None

    return ProductReadDTO(**json.loads(cached_product), cache="hit")


async def load_product_from_primary(
    client: redis.Redis,
    product_id: int,
    redis_key: str,
    *,
    simulate_slow_source: bool,
) -> dict[str, int | str]:
    """模拟数据源读取，并写入正常缓存或短 TTL 空值缓存。"""
    await client.hincrby(PRIMARY_READS_KEY, "products", 1)
    if simulate_slow_source:
        await asyncio.sleep(0.2)

    product = products.get(product_id)
    if product is None:
        await client.set(redis_key, NOT_FOUND_SENTINEL, ex=NOT_FOUND_TTL_SECONDS)
        raise product_not_found_error()

    await client.set(redis_key, json.dumps(product), ex=120)
    return product


# Hash 字段：统计「真正打到主库」的次数，用来验证 Cache Aside
PRIMARY_READS_KEY = "lab:stats:primary_reads"
NOT_FOUND_SENTINEL = "__NOT_FOUND__"
NOT_FOUND_TTL_SECONDS = 30
REBUILD_LOCK_TTL_SECONDS = 5
REBUILD_WAIT_ATTEMPTS = 30
REBUILD_WAIT_SECONDS = 0.03

# 只能删除仍由自己持有的锁，避免锁过期并被接管后误删其他请求的锁。
RELEASE_LOCK_LUA = """
if redis.call('get', KEYS[1]) == ARGV[1] then
    return redis.call('del', KEYS[1])
end
return 0
"""

# 将 INCR 与首次设置过期时间放入同一 Lua 脚本，避免进程在两条命令之间
# 崩溃，留下一个永不过期的限流计数器。
FIXED_WINDOW_RATE_LIMIT_LUA = """
local count = redis.call('incr', KEYS[1])
if count == 1 then
    redis.call('expire', KEYS[1], ARGV[1])
end
return count
"""
@app.get("/health")
async def health(request: Request) -> dict[str, str]:
    """健康检查：确认 Redis 还能 ping 通。"""
    await request.app.state.redis.ping()
    return {"status": "ok", "redis": "connected"}


@app.put("/cache/{key}", response_model=CacheReadDTO)
async def write_cache(
    key: str,
    payload: CacheWriteDTO,
    request: Request,
) -> CacheReadDTO:
    """直接写 Redis：练习 SET + TTL。"""
    redis_key = cache_key(key)
    client: redis.Redis = request.app.state.redis
    # ex=秒：过期后自动删除，避免永久脏数据
    await client.set(redis_key, payload.value, ex=payload.ttl_seconds)
    return CacheReadDTO(
        key=redis_key,
        value=payload.value,
        ttl_seconds=payload.ttl_seconds,
    )


@app.get("/cache/{key}", response_model=CacheReadDTO)
async def read_cache(key: str, request: Request) -> CacheReadDTO:
    """直接读 Redis：练习 GET / TTL；不存在则 404（纯缓存 miss）。"""
    redis_key = cache_key(key)
    client: redis.Redis = request.app.state.redis
    # mget 返回列表；单 key 时取 value[0]
    value, ttl_seconds = await client.mget(redis_key), await client.ttl(redis_key)

    if value[0] is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"code": "CACHE_MISS",
                    "message": "Cache key was not found"},
        )

    return CacheReadDTO(
        key=redis_key,
        value=value[0],
        ttl_seconds=ttl_seconds,
    )


@app.get("/products/{product_id}", response_model=ProductReadDTO)
async def get_product(
    product_id: int,
    request: Request,
    simulate_slow_source: bool = False,
    protect_stampede: bool = False,
) -> ProductReadDTO:
    """
    Cache Aside 读路径：
    1. 先查缓存
    2. 命中 → 直接返回（hit）
    3. 未命中 → 查主库 → 回填缓存 → 返回（miss）
    """
    client: redis.Redis = request.app.state.redis
    redis_key = product_cache_key(product_id)
    cached = await cached_product_or_none(client, redis_key)
    if cached is not None:
        return cached

    if not protect_stampede:
        product = await load_product_from_primary(
            client,
            product_id,
            redis_key,
            simulate_slow_source=simulate_slow_source,
        )
        return ProductReadDTO(**product, cache="miss")

    # SET NX EX 是原子操作：只有一个请求能创建这把短期重建锁。
    lock_key = rebuild_lock_key(product_id)
    token = str(uuid4())
    acquired = await client.set(
        lock_key,
        token,
        nx=True,
        ex=REBUILD_LOCK_TTL_SECONDS,
    )

    if acquired:
        try:
            # 获得锁后再检查一次，避免刚好有人已经完成回填。
            cached = await cached_product_or_none(client, redis_key)
            if cached is not None:
                return cached

            product = await load_product_from_primary(
                client,
                product_id,
                redis_key,
                simulate_slow_source=simulate_slow_source,
            )
            return ProductReadDTO(**product, cache="miss")
        finally:
            await client.eval(RELEASE_LOCK_LUA, 1, lock_key, token)

    # 没拿到锁：不回源，等待持锁请求把缓存重建好。
    for _ in range(REBUILD_WAIT_ATTEMPTS):
        await asyncio.sleep(REBUILD_WAIT_SECONDS)
        cached = await cached_product_or_none(client, redis_key)
        if cached is not None:
            return cached

    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        detail={"code": "CACHE_REBUILDING", "message": "Try again shortly"},
    )


@app.get("/lab/rate-limit/{client_id}")
async def fixed_window_rate_limit(
    client_id: str,
    request: Request,
    limit: int = 3,
    window_seconds: int = 10,
) -> dict[str, object]:
    """实验接口：每个 client_id 在一个固定窗口内最多通过 limit 次。"""
    if limit < 1 or window_seconds < 1:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="limit and window_seconds must be positive",
        )

    redis_key = f"rate_limit:lab:{client_id}"
    count = await request.app.state.redis.eval(
        FIXED_WINDOW_RATE_LIMIT_LUA,
        1,
        redis_key,
        window_seconds,
    )
    ttl = await request.app.state.redis.ttl(redis_key)
    if count > limit:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail={"code": "RATE_LIMITED", "retry_after_seconds": ttl},
            headers={"Retry-After": str(max(ttl, 0))},
        )

    return {"allowed": True, "count": count, "limit": limit, "ttl": ttl}


@app.get("/debug/primary-reads")
async def primary_reads(request: Request) -> dict[str, int]:
    """调试接口：看商品读请求打到主库多少次。"""
    reads = await request.app.state.redis.hget(PRIMARY_READS_KEY, "products")
    return {"products": int(reads or 0)}


@app.patch("/products/{product_id}")
async def update_product(
    product_id: int,
    payload: ProductUpdateDTO,
    request: Request,
) -> dict[str, object]:
    """
    Cache Aside 写路径：
    先更新主库，再删除缓存（失效），避免读到旧值。
    下次 GET 会 miss 并回填最新数据。
    """
    product = products.get(product_id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"code": "PRODUCT_NOT_FOUND",
                    "message": "Product was not found"},
        )

    # 更新「主库」
    product.update(payload.model_dump(exclude_unset=True))
    # 失效对应缓存；不要边写库边更新缓存（并发下更易脏读）
    await request.app.state.redis.delete(product_cache_key(product_id))
    return {"product": product, "cache_invalidated": True}
