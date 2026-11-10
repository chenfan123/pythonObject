import pytest

from examples.retry_policy import retry_on_timeout


class FakeModelClient:
    def __init__(self, outcomes: list[object]) -> None:
        self._outcomes = outcomes
        self.calls = 0

    async def call(self) -> str:
        self.calls += 1
        outcome = self._outcomes.pop(0)
        if isinstance(outcome, BaseException):
            raise outcome
        return str(outcome)


class FakeSleeper:
    def __init__(self) -> None:
        self.delays: list[float] = []

    async def __call__(self, delay: float) -> None:
        self.delays.append(delay)


@pytest.mark.asyncio
async def test_retry_succeeds_after_one_timeout_without_real_waiting() -> None:
    client = FakeModelClient([TimeoutError(), "model-result"])
    sleeper = FakeSleeper()

    result = await retry_on_timeout(
        client.call,
        max_attempts=3,
        sleep=sleeper,
    )

    assert result == "model-result"
    assert client.calls == 2
    assert sleeper.delays == [0.1]


@pytest.mark.asyncio
async def test_retry_stops_after_max_attempts() -> None:
    client = FakeModelClient([TimeoutError(), TimeoutError(), TimeoutError()])
    sleeper = FakeSleeper()

    with pytest.raises(TimeoutError):
        await retry_on_timeout(client.call, max_attempts=3, sleep=sleeper)

    assert client.calls == 3
    assert sleeper.delays == [0.1, 0.2]


@pytest.mark.asyncio
async def test_retry_does_not_retry_non_timeout_error() -> None:
    client = FakeModelClient([ValueError("invalid request")])
    sleeper = FakeSleeper()

    with pytest.raises(ValueError, match="invalid request"):
        await retry_on_timeout(client.call, max_attempts=3, sleep=sleeper)

    assert client.calls == 1
    assert sleeper.delays == []
