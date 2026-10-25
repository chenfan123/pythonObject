import os
from types import SimpleNamespace

# 该测试替换了数据库依赖，不会实际连库；应用导入时仍需要配置值。
os.environ.setdefault(
    "DATABASE_URL",
    "postgresql+asyncpg://test:test@127.0.0.1:1/test_db",
)

from fastapi.testclient import TestClient

from app.core.domain_errors import EmailAlreadyExistsError, UserNotFoundError
from app.dependencies.users import get_user_service
from app.main import app


class FakeUserService:
    """接口测试使用的替身：不连接 PostgreSQL。"""

    _users = [
        SimpleNamespace(id=10, email="alice@example.com", password_hash="hash-a"),
        SimpleNamespace(id=20, email="bob@example.com", password_hash="hash-b"),
        SimpleNamespace(id=30, email="carol@example.com", password_hash="hash-c"),
    ]

    async def list_users(
        self,
        *,
        keyword: str | None,
        email_domain: str | None,
        offset: int,
        limit: int,
    ) -> tuple[list[SimpleNamespace], int]:
        filtered_users = self._users
        if keyword is not None:
            filtered_users = [
                user for user in filtered_users if keyword.lower() in user.email.lower()
            ]
        if email_domain is not None:
            filtered_users = [
                user
                for user in filtered_users
                if user.email.lower().endswith(f"@{email_domain.lower()}")
            ]
        return filtered_users[offset : offset + limit], len(filtered_users)

    async def create_user(self, *, email: str, password: str) -> SimpleNamespace:
        if email == "taken@example.com":
            raise EmailAlreadyExistsError()

        return SimpleNamespace(id=101, email=email)

    async def update_user_email(self, *, user_id: int, email: str) -> SimpleNamespace:
        user = next((user for user in self._users if user.id == user_id), None)
        if user is None:
            raise UserNotFoundError()
        if any(
            existing.id != user_id and existing.email.lower() == email.lower()
            for existing in self._users
        ):
            raise EmailAlreadyExistsError()
        return SimpleNamespace(id=user_id, email=email, password_hash="new-hash")

    async def delete_user(self, *, user_id: int) -> None:
        if not any(user.id == user_id for user in self._users):
            raise UserNotFoundError()


def get_fake_user_service() -> FakeUserService:
    return FakeUserService()


def setup_module() -> None:
    app.dependency_overrides[get_user_service] = get_fake_user_service


def teardown_module() -> None:
    app.dependency_overrides.clear()


def test_create_user_returns_public_fields() -> None:
    with TestClient(app) as client:
        response = client.post(
            "/users",
            json={"email": "alice@example.com", "password": "safe-password"},
        )

    assert response.status_code == 201
    assert response.json() == {"id": 101, "email": "alice@example.com"}


def test_create_user_duplicate_email_returns_conflict() -> None:
    with TestClient(app) as client:
        response = client.post(
            "/users",
            json={"email": "taken@example.com", "password": "safe-password"},
        )

    assert response.status_code == 409
    assert response.json() == {
        "code": "EMAIL_ALREADY_EXISTS",
        "message": "Email already exists",
    }


def test_list_users_paginates_and_hides_password_hash() -> None:
    with TestClient(app) as client:
        response = client.get("/users?offset=1&limit=2")

    assert response.status_code == 200
    assert response.json() == {
        "items": [
            {"id": 20, "email": "bob@example.com"},
            {"id": 30, "email": "carol@example.com"},
        ],
        "total": 3,
        "offset": 1,
        "limit": 2,
    }


def test_list_users_uses_keyword_for_items_and_total() -> None:
    with TestClient(app) as client:
        response = client.get("/users?keyword=ALICE")

    assert response.status_code == 200
    assert response.json() == {
        "items": [{"id": 10, "email": "alice@example.com"}],
        "total": 1,
        "offset": 0,
        "limit": 20,
    }


def test_list_users_combines_keyword_and_email_domain() -> None:
    with TestClient(app) as client:
        response = client.get("/users?keyword=alice&email_domain=example.com")

    assert response.status_code == 200
    assert response.json()["items"] == [{"id": 10, "email": "alice@example.com"}]
    assert response.json()["total"] == 1


def test_update_user_email_returns_public_fields() -> None:
    with TestClient(app) as client:
        response = client.patch(
            "/users/10",
            json={"email": "alice-new@example.com"},
        )

    assert response.status_code == 200
    assert response.json() == {"id": 10, "email": "alice-new@example.com"}


def test_update_user_email_handles_missing_and_duplicate_users() -> None:
    with TestClient(app) as client:
        missing_response = client.patch(
            "/users/999", json={"email": "nobody@example.com"}
        )
        duplicate_response = client.patch(
            "/users/10", json={"email": "bob@example.com"}
        )

    assert missing_response.status_code == 404
    assert missing_response.json()["code"] == "USER_NOT_FOUND"
    assert duplicate_response.status_code == 409
    assert duplicate_response.json()["code"] == "EMAIL_ALREADY_EXISTS"


def test_delete_user_returns_no_content_or_not_found() -> None:
    with TestClient(app) as client:
        deleted_response = client.delete("/users/10")
        missing_response = client.delete("/users/999")

    assert deleted_response.status_code == 204
    assert deleted_response.content == b""
    assert missing_response.status_code == 404
    assert missing_response.json()["code"] == "USER_NOT_FOUND"
