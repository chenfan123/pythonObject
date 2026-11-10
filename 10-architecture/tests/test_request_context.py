from app.core.request_context import get_request_id, reset_request_id, set_request_id


def test_request_context_value_is_scoped_and_resettable() -> None:
    assert get_request_id() is None

    token = set_request_id("trace-123")
    assert get_request_id() == "trace-123"

    reset_request_id(token)
    assert get_request_id() is None
