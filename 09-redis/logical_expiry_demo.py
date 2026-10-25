"""逻辑过期：旧值可用时，读取不等待；只有一个后台任务刷新。"""

import asyncio
from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class CachedValue:
    data: dict[str, object]
    expire_at: datetime


cache = CachedValue(
    data={"id": 42, "name": "Keyboard", "price": 99},
    # 故意设为过去，让本次读取进入“逻辑过期”分支。
    expire_at=datetime.now() - timedelta(seconds=1),
)
refresh_lock = asyncio.Lock()


async def rebuild_cache() -> None:
    global cache
    print("  [后台] 开始从数据源刷新缓存")
    await asyncio.sleep(0.2)  # 模拟慢速 I/O
    cache = CachedValue(
        data={"id": 42, "name": "Keyboard", "price": 109},
        expire_at=datetime.now() + timedelta(seconds=30),
    )
    print("  [后台] 刷新完成，价格更新为 109")


async def refresh_once_in_background() -> None:
    if refresh_lock.locked():
        return

    async with refresh_lock:
        # 双重检查：等待锁的期间，可能已经被别的任务更新了。
        if cache.expire_at > datetime.now():
            return
        await rebuild_cache()


async def get_product(request_name: str) -> dict[str, object]:
    is_expired = cache.expire_at <= datetime.now()
    if is_expired:
        print(f"{request_name}: 缓存逻辑过期，立即返回旧价格 {cache.data['price']}")
        asyncio.create_task(refresh_once_in_background())
    else:
        print(f"{request_name}: 缓存新鲜，返回价格 {cache.data['price']}")
    return cache.data


async def main() -> None:
    print("三个请求同时到达：")
    first_results = await asyncio.gather(
        get_product("请求 A"),
        get_product("请求 B"),
        get_product("请求 C"),
    )
    print("本轮用户拿到的价格:", [item["price"] for item in first_results])

    await asyncio.sleep(0.3)
    latest = await get_product("刷新后的请求 D")
    print("请求 D 拿到的价格:", latest["price"])


asyncio.run(main())
