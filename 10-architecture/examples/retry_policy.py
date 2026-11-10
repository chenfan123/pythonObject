"""可替换等待函数的最小异步重试策略示例。"""

import asyncio
from collections.abc import Awaitable, Callable
from typing import TypeVar


T = TypeVar("T")
Sleeper = Callable[[float], Awaitable[None]]
Operation = Callable[[], Awaitable[T]]


async def retry_on_timeout(
    operation: Operation[T],
    *,
    max_attempts: int,
    base_delay_seconds: float = 0.1,
    sleep: Sleeper = asyncio.sleep,
) -> T:
    """仅重试 TimeoutError；等待时间按 0.1、0.2、0.4... 指数增长。"""
    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")

    for attempt in range(max_attempts):
        try:
            return await operation()
        except TimeoutError:
            if attempt == max_attempts - 1:
                raise
            await sleep(base_delay_seconds * (2**attempt))

    raise AssertionError("unreachable")
