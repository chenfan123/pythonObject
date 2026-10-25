"""Redis Sorted Set + Lua 的滑动窗口限流实验。"""

import math
import time
from contextlib import asynccontextmanager
from uuid import uuid4

import redis.asyncio as redis
from fastapi import FastAPI, HTTPException, Request, status


REDIS_URL = "redis://localhost:6380/0"

# 返回：是否放行、窗口内数量、最早请求的毫秒时间戳（拒绝时才有值）。
SLIDING_WINDOW_LUA = """
local key = KEYS[1]
local now_ms = tonumber(ARGV[1])
local window_ms = tonumber(ARGV[2])
local limit = tonumber(ARGV[3])
local request_id = ARGV[4]

redis.call('ZREMRANGEBYSCORE', key, 0, now_ms - window_ms)
local count = redis.call('ZCARD', key)
if count >= limit then
    local oldest = redis.call('ZRANGE', key, 0, 0, 'WITHSCORES')[2]
    return {0, count, oldest}
end

redis.call('ZADD', key, now_ms, request_id)
redis.call('EXPIRE', key, math.ceil(window_ms / 1000))
return {1, count + 1, 0}
"""


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = redis.from_url(REDIS_URL, decode_responses=True)
    await client.ping()
    app.state.redis = client
    try:
        yield
    finally:
        await client.aclose()


app = FastAPI(title="Redis Sliding Window Rate Limit Lab", lifespan=lifespan)


def rate_limit_key(client_id: str) -> str:
    return f"rate_limit:sliding:lab:{client_id}"


@app.get("/lab/sliding-rate-limit/{client_id}")
async def sliding_rate_limit(
    client_id: str,
    request: Request,
    limit: int = 3,
    window_seconds: int = 10,
) -> dict[str, int | bool]:
    if limit < 1 or window_seconds < 1:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="limit and window_seconds must be positive",
        )

    now_ms = int(time.time() * 1000)
    window_ms = window_seconds * 1000
    allowed, count, oldest_ms = await request.app.state.redis.eval(
        SLIDING_WINDOW_LUA,
        1,
        rate_limit_key(client_id),
        now_ms,
        window_ms,
        limit,
        str(uuid4()),
    )
    if not allowed:
        retry_after = max(1, math.ceil((int(oldest_ms) + window_ms - now_ms) / 1000))
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail={"code": "RATE_LIMITED", "retry_after_seconds": retry_after},
            headers={"Retry-After": str(retry_after)},
        )
    return {"allowed": True, "count": int(count), "limit": limit}
