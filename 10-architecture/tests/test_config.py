import pytest
from pydantic import ValidationError

from app.core.config import Settings


def test_settings_converts_string_page_size_to_integer() -> None:
    settings = Settings(
        database_url="postgresql+asyncpg://test:test@localhost:5432/test",
        max_page_size="200",
    )

    assert settings.max_page_size == 200


def test_settings_rejects_invalid_page_size_before_application_starts() -> None:
    with pytest.raises(ValidationError):
        Settings(
            database_url="postgresql+asyncpg://test:test@localhost:5432/test",
            max_page_size=0,
        )
