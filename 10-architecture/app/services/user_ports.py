"""UserService 依赖的能力契约，而非具体数据库实现。"""

from typing import AsyncContextManager, Protocol

from app.models.user import UserORM


class UserRepositoryPort(Protocol):
    async def get_by_email(self, email: str) -> UserORM | None: ...

    async def get_by_id(self, user_id: int) -> UserORM | None: ...

    async def list(
        self,
        *,
        keyword: str | None,
        email_domain: str | None,
        offset: int,
        limit: int,
    ) -> list[UserORM]: ...

    async def count(self, *, keyword: str | None, email_domain: str | None) -> int: ...

    async def update_email(self, *, user_id: int, email: str) -> UserORM | None: ...

    async def delete_by_id(self, user_id: int) -> bool: ...

    def add(self, user: UserORM) -> None: ...


class UserSettingsRepositoryPort(Protocol):
    def add_default_for_user(self, user_id: int) -> None: ...


class TransactionPort(Protocol):
    """UserService 需要的最小事务能力；真实 AsyncSession 结构上满足它。"""

    def begin(self) -> AsyncContextManager[object]: ...

    async def flush(self) -> None: ...

    async def refresh(self, instance: object) -> None: ...
