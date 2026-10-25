import pytest

from app.core.domain_errors import UserNotFoundError
from app.models.user import UserORM
from app.services.user_service import UserService


class FakeUserRepository:
    """仅用内存模拟 Repository；不实现 SQLAlchemy。"""

    def __init__(self, users: list[UserORM]) -> None:
        self._users = users

    async def get_by_email(self, email: str) -> UserORM | None:
        return next((user for user in self._users if user.email == email), None)

    async def get_by_id(self, user_id: int) -> UserORM | None:
        return next((user for user in self._users if user.id == user_id), None)

    async def list(
        self,
        *,
        keyword: str | None,
        email_domain: str | None,
        offset: int,
        limit: int,
    ) -> list[UserORM]:
        users = self._users
        if keyword is not None:
            users = [user for user in users if keyword.lower() in user.email.lower()]
        if email_domain is not None:
            users = [
                user
                for user in users
                if user.email.lower().endswith(f"@{email_domain.lower()}")
            ]
        return users[offset : offset + limit]

    async def count(self, *, keyword: str | None, email_domain: str | None) -> int:
        return len(
            await self.list(
                keyword=keyword,
                email_domain=email_domain,
                offset=0,
                limit=len(self._users),
            )
        )

    async def update_email(self, *, user_id: int, email: str) -> UserORM | None:
        user = await self.get_by_id(user_id)
        if user is not None:
            user.email = email
        return user

    async def delete_by_id(self, user_id: int) -> bool:
        user = await self.get_by_id(user_id)
        if user is None:
            return False
        self._users.remove(user)
        return True

    def add(self, user: UserORM) -> None:
        self._users.append(user)


class FakeUserSettingsRepository:
    def __init__(self) -> None:
        self.created_for_user_ids: list[int] = []

    def add_default_for_user(self, user_id: int) -> None:
        self.created_for_user_ids.append(user_id)


class FailingUserSettingsRepository(FakeUserSettingsRepository):
    def add_default_for_user(self, user_id: int) -> None:
        raise RuntimeError("settings storage is unavailable")


class FakeTransaction:
    def __init__(self, session: "FakeTransactionSession") -> None:
        self._session = session
        self._users_before_transaction: list[UserORM] = []

    async def __aenter__(self) -> "FakeTransaction":
        self._session.started = True
        self._users_before_transaction = list(self._session._user_repository._users)
        return self

    async def __aexit__(self, exc_type: object, exc: object, traceback: object) -> bool:
        if exc_type is None:
            self._session.committed = True
        else:
            self._session.rolled_back = True
            self._session._user_repository._users[:] = self._users_before_transaction
        return False


class FakeTransactionSession:
    """只模拟本 Service 用到的 Session 能力，不连接数据库。"""

    def __init__(self, user_repository: FakeUserRepository) -> None:
        self._user_repository = user_repository
        self.started = False
        self.committed = False
        self.rolled_back = False
        self.flush_calls = 0

    def begin(self) -> FakeTransaction:
        return FakeTransaction(self)

    async def flush(self) -> None:
        self.flush_calls += 1
        for index, user in enumerate(self._user_repository._users, start=1):
            if user.id is None:
                user.id = index

    async def refresh(self, instance: object) -> None:
        pass


def make_service(
    users: list[UserORM],
) -> tuple[UserService, FakeTransactionSession, FakeUserSettingsRepository]:
    user_repository = FakeUserRepository(users)
    settings_repository = FakeUserSettingsRepository()
    transaction = FakeTransactionSession(user_repository)
    return UserService(
        user_repository, settings_repository, transaction
    ), transaction, settings_repository


@pytest.mark.asyncio
async def test_get_user_uses_fake_repository_without_database() -> None:
    user = UserORM(id=7, email="alice@example.com", password_hash="secret-hash")
    service, _, _ = make_service([user])

    result = await service.get_user(7)

    assert result is user


@pytest.mark.asyncio
async def test_get_user_raises_domain_error_when_fake_repository_has_no_user() -> None:
    service, _, _ = make_service([])

    with pytest.raises(UserNotFoundError):
        await service.get_user(404)


@pytest.mark.asyncio
async def test_list_users_returns_page_and_total_from_same_fake_repository() -> None:
    users = [
        UserORM(id=1, email="alice@example.com", password_hash="a"),
        UserORM(id=2, email="bob@other.com", password_hash="b"),
    ]
    service, _, _ = make_service(users)

    page, total = await service.list_users(
        keyword=None,
        email_domain="example.com",
        offset=0,
        limit=20,
    )

    assert [user.id for user in page] == [1]
    assert total == 1


@pytest.mark.asyncio
async def test_create_user_uses_one_transaction_for_user_and_default_settings() -> None:
    service, transaction, settings_repository = make_service([])

    user = await service.create_user(
        email="new@example.com",
        password="safe-password",
    )

    assert transaction.started is True
    assert transaction.committed is True
    assert transaction.rolled_back is False
    assert transaction.flush_calls == 1
    assert user.id == 1
    assert settings_repository.created_for_user_ids == [1]


@pytest.mark.asyncio
async def test_create_user_rolls_back_when_default_settings_creation_fails() -> None:
    user_repository = FakeUserRepository([])
    settings_repository = FailingUserSettingsRepository()
    transaction = FakeTransactionSession(user_repository)
    service = UserService(user_repository, settings_repository, transaction)

    with pytest.raises(RuntimeError, match="settings storage is unavailable"):
        await service.create_user(
            email="new@example.com",
            password="safe-password",
        )

    assert transaction.committed is False
    assert transaction.rolled_back is True
    assert user_repository._users == []
