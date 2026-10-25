import pytest

from examples.agent_task_domain import (
    AgentTask,
    InvalidTaskTransitionError,
    TaskStatus,
)


def test_running_task_can_be_cancelled_after_worker_confirms() -> None:
    task = AgentTask(id=1, status=TaskStatus.QUEUED)

    task.start()
    task.request_cancel()
    task.confirm_cancel()

    assert task.status == TaskStatus.CANCELLED


def test_queued_task_can_be_cancelled_without_waiting_for_a_worker() -> None:
    task = AgentTask(id=2, status=TaskStatus.QUEUED)

    task.request_cancel()

    assert task.status == TaskStatus.CANCELLED


def test_finished_task_cannot_restart_or_be_cancelled() -> None:
    task = AgentTask(id=3, status=TaskStatus.QUEUED)
    task.start()
    task.succeed()

    with pytest.raises(InvalidTaskTransitionError):
        task.start()
    with pytest.raises(InvalidTaskTransitionError):
        task.request_cancel()
