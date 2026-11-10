"""进程内幂等 Worker 示例：真实多实例场景应把去重状态放入数据库或 Redis。"""

import asyncio
from collections.abc import Awaitable, Callable
from dataclasses import dataclass


@dataclass(frozen=True)
class OutboxEvent:
    event_id: str
    event_type: str
    payload: dict[str, object]


class InMemoryEventDeduplicator:
    def __init__(self) -> None:
        self._completed: set[str] = set()
        self._in_progress: set[str] = set()
        self._lock = asyncio.Lock()

    async def claim(self, event_id: str) -> bool:
        """只有尚未完成、且没有其他协程正在处理的事件能抢到处理权。"""
        async with self._lock:
            if event_id in self._completed or event_id in self._in_progress:
                return False
            self._in_progress.add(event_id)
            return True

    async def mark_completed(self, event_id: str) -> None:
        async with self._lock:
            self._in_progress.discard(event_id)
            self._completed.add(event_id)

    async def release(self, event_id: str) -> None:
        """处理失败时释放占用，让后续投递能重试。"""
        async with self._lock:
            self._in_progress.discard(event_id)


EventHandler = Callable[[OutboxEvent], Awaitable[None]]


class IdempotentWorker:
    def __init__(self, deduplicator: InMemoryEventDeduplicator) -> None:
        self._deduplicator = deduplicator

    async def process(self, event: OutboxEvent, handler: EventHandler) -> bool:
        """返回 True 表示本次真正处理；False 表示重复投递而跳过。"""
        if not await self._deduplicator.claim(event.event_id):
            return False

        try:
            await handler(event)
        except Exception:
            await self._deduplicator.release(event.event_id)
            raise

        await self._deduplicator.mark_completed(event.event_id)
        return True
