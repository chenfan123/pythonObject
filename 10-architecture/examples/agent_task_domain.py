"""Agent 长任务的领域状态机示例：不依赖 FastAPI 或数据库。"""

from dataclasses import dataclass
from enum import StrEnum


class TaskStatus(StrEnum):
    QUEUED = "queued"
    RUNNING = "running"
    CANCEL_REQUESTED = "cancel_requested"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"


class InvalidTaskTransitionError(ValueError):
    """任务当前状态不允许执行该业务动作。"""


@dataclass
class AgentTask:
    id: int
    status: TaskStatus

    def start(self) -> None:
        if self.status != TaskStatus.QUEUED:
            raise InvalidTaskTransitionError("Only queued tasks can start")
        self.status = TaskStatus.RUNNING

    def request_cancel(self) -> None:
        if self.status == TaskStatus.QUEUED:
            self.status = TaskStatus.CANCELLED
            return
        if self.status == TaskStatus.RUNNING:
            self.status = TaskStatus.CANCEL_REQUESTED
            return
        raise InvalidTaskTransitionError("Task cannot be cancelled now")

    def succeed(self) -> None:
        if self.status != TaskStatus.RUNNING:
            raise InvalidTaskTransitionError("Only running tasks can succeed")
        self.status = TaskStatus.SUCCEEDED

    def confirm_cancel(self) -> None:
        if self.status != TaskStatus.CANCEL_REQUESTED:
            raise InvalidTaskTransitionError("Cancellation was not requested")
        self.status = TaskStatus.CANCELLED
