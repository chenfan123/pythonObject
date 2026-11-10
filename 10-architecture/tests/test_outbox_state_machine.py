from datetime import UTC, datetime, timedelta

from examples.outbox_state_machine import OutboxEvent, OutboxStatus


NOW = datetime(2026, 10, 27, 9, 0, tzinfo=UTC)


def make_event() -> OutboxEvent:
    return OutboxEvent(event_id="outbox-9001", available_at=NOW)


def test_pending_event_can_be_claimed_by_only_one_worker() -> None:
    event = make_event()

    assert event.claim(worker_id="worker-a", now=NOW) is True
    assert event.claim(worker_id="worker-b", now=NOW) is False
    assert event.status == OutboxStatus.PROCESSING
    assert event.locked_by == "worker-a"


def test_retry_uses_backoff_then_event_can_be_sent() -> None:
    event = make_event()
    event.claim(worker_id="worker-a", now=NOW)

    event.schedule_retry(
        now=NOW,
        error="model timeout",
        max_attempts=3,
        base_delay_seconds=10,
    )

    assert event.status == OutboxStatus.PENDING
    assert event.attempts == 1
    assert event.available_at == NOW + timedelta(seconds=10)
    assert event.claim(worker_id="worker-b", now=NOW + timedelta(seconds=9)) is False
    assert event.claim(worker_id="worker-b", now=NOW + timedelta(seconds=10)) is True

    event.mark_sent(now=NOW + timedelta(seconds=11))
    assert event.status == OutboxStatus.SENT


def test_event_becomes_failed_after_max_attempts() -> None:
    event = make_event()
    event.claim(worker_id="worker-a", now=NOW)

    event.schedule_retry(
        now=NOW,
        error="model timeout",
        max_attempts=1,
    )

    assert event.status == OutboxStatus.FAILED
    assert event.attempts == 1


def test_expired_processing_lease_can_be_reclaimed() -> None:
    event = make_event()
    event.claim(worker_id="worker-a", now=NOW)

    assert event.reclaim_if_lock_expired(
        now=NOW + timedelta(seconds=29),
        lease=timedelta(seconds=30),
    ) is False
    assert event.reclaim_if_lock_expired(
        now=NOW + timedelta(seconds=30),
        lease=timedelta(seconds=30),
    ) is True
    assert event.status == OutboxStatus.PENDING
    assert event.locked_by is None
