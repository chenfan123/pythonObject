"""Outbox 事件生命周期的纯领域模型示例。"""

from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import StrEnum


class OutboxStatus(StrEnum):
    PENDING = "pending"
    PROCESSING = "processing"
    SENT = "sent"
    FAILED = "failed"


class InvalidOutboxTransitionError(ValueError):
    pass


@dataclass
class OutboxEvent:
    event_id: str
    available_at: datetime
    status: OutboxStatus = OutboxStatus.PENDING
    attempts: int = 0
    locked_at: datetime | None = None
    locked_by: str | None = None
    sent_at: datetime | None = None
    last_error: str | None = None

    def claim(self, *, worker_id: str, now: datetime) -> bool:
        if self.status != OutboxStatus.PENDING or now < self.available_at:
            return False
        self.status = OutboxStatus.PROCESSING
        self.locked_at = now
        self.locked_by = worker_id
        return True

    def mark_sent(self, *, now: datetime) -> None:
        if self.status != OutboxStatus.PROCESSING:
            raise InvalidOutboxTransitionError("Only processing events can be sent")
        self.status = OutboxStatus.SENT
        self.sent_at = now
        self.locked_at = None
        self.locked_by = None

    def schedule_retry(
        self,
        *,
        now: datetime,
        error: str,
        max_attempts: int,
        base_delay_seconds: float = 1.0,
    ) -> None:
        if self.status != OutboxStatus.PROCESSING:
            raise InvalidOutboxTransitionError("Only processing events can be retried")

        self.attempts += 1
        self.last_error = error
        self.locked_at = None
        self.locked_by = None

        if self.attempts >= max_attempts:
            self.status = OutboxStatus.FAILED
            return

        self.status = OutboxStatus.PENDING
        self.available_at = now + timedelta(
            seconds=base_delay_seconds * (2 ** (self.attempts - 1))
        )

    def reclaim_if_lock_expired(self, *, now: datetime, lease: timedelta) -> bool:
        if (
            self.status != OutboxStatus.PROCESSING
            or self.locked_at is None
            or now < self.locked_at + lease
        ):
            return False

        self.status = OutboxStatus.PENDING
        self.locked_at = None
        self.locked_by = None
        self.available_at = now
        return True
