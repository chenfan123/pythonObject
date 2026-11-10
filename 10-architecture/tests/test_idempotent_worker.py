import asyncio

import pytest

from examples.idempotent_worker import (
    IdempotentWorker,
    InMemoryEventDeduplicator,
    OutboxEvent,
)


def make_event() -> OutboxEvent:
    return OutboxEvent(
        event_id="event-9001",
        event_type="welcome_email",
        payload={"user_id": 42},
    )


@pytest.mark.asyncio
async def test_duplicate_event_is_handled_only_once() -> None:
    worker = IdempotentWorker(InMemoryEventDeduplicator())
    handled_event_ids: list[str] = []

    async def handler(event: OutboxEvent) -> None:
        handled_event_ids.append(event.event_id)

    assert await worker.process(make_event(), handler) is True
    assert await worker.process(make_event(), handler) is False
    assert handled_event_ids == ["event-9001"]


@pytest.mark.asyncio
async def test_concurrent_duplicate_events_have_one_handler_execution() -> None:
    worker = IdempotentWorker(InMemoryEventDeduplicator())
    handled_event_ids: list[str] = []

    async def handler(event: OutboxEvent) -> None:
        await asyncio.sleep(0)
        handled_event_ids.append(event.event_id)

    results = await asyncio.gather(
        worker.process(make_event(), handler),
        worker.process(make_event(), handler),
    )

    assert results.count(True) == 1
    assert results.count(False) == 1
    assert handled_event_ids == ["event-9001"]


@pytest.mark.asyncio
async def test_failed_event_is_released_for_later_retry() -> None:
    worker = IdempotentWorker(InMemoryEventDeduplicator())
    attempts = 0

    async def fails_once_then_succeeds(_event: OutboxEvent) -> None:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            raise TimeoutError()

    with pytest.raises(TimeoutError):
        await worker.process(make_event(), fails_once_then_succeeds)

    assert await worker.process(make_event(), fails_once_then_succeeds) is True
    assert attempts == 2
