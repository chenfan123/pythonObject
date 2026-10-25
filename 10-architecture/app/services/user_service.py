import base64
import hashlib
import secrets

from sqlalchemy.exc import IntegrityError
from app.core.domain_errors import EmailAlreadyExistsError, UserNotFoundError
from app.models.user import UserORM
from app.services.user_ports import (
    TransactionPort,
    UserRepositoryPort,
    UserSettingsRepositoryPort,
)


def hash_password(password: str) -> str:
    """示例密码哈希；认证章节会进一步讨论参数、升级和校验。"""
    salt = secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 600_000)
    return "pbkdf2_sha256$600000$" + base64.b64encode(salt + digest).decode()


class UserService:
    def __init__(
        self,
        user_repository: UserRepositoryPort,
        settings_repository: UserSettingsRepositoryPort,
        transaction: TransactionPort,
    ) -> None:
        self._user_repository = user_repository
        self._settings_repository = settings_repository
        self._transaction = transaction

    async def create_user(self, *, email: str, password: str) -> UserORM:
        try:
            # 一个事务内协调两张表：要么用户和默认设置都创建，要么都不创建。异常发生时自动 rollback，避免 Session 留在失败事务中
            async with self._transaction.begin():
                if await self._user_repository.get_by_email(email) is not None:
                    raise EmailAlreadyExistsError

                user = UserORM(
                    email=email, password_hash=hash_password(password))
                self._user_repository.add(user)  # 告诉 SQLAlchemy：“这个对象稍后要插入。”
                # flush 发出 INSERT 并取得数据库生成的 user.id，但尚未 commit。
                await self._transaction.flush()  # 会立刻把 INSERT 发到 PostgreSQL
                self._settings_repository.add_default_for_user(user.id)
        except IntegrityError as error:  # 数据库拒绝了违反约束的写入。
            raise EmailAlreadyExistsError from error  # 保留原始数据库异常作为调试线索，但对上层只暴露清晰的领域含义。

        await self._transaction.refresh(user)  # 更新 user 对象，使其包含数据库生成的 id 和其他可能的变更。
        return user

    async def get_user(self, user_id: int) -> UserORM:
        user = await self._user_repository.get_by_id(user_id)
        if user is None:
            raise UserNotFoundError
        return user

    async def list_users(
        self,
        *,
        keyword: str | None,
        email_domain: str | None,
        offset: int,
        limit: int,
    ) -> tuple[list[UserORM], int]:
        """列表业务目前无额外权限规则，保留 Service 边界供后续扩展。"""
        users = await self._user_repository.list(
            keyword=keyword,
            email_domain=email_domain,
            offset=offset,
            limit=limit,
        )
        total = await self._user_repository.count(
            keyword=keyword, email_domain=email_domain
        )
        return users, total

    async def update_user_email(self, *, user_id: int, email: str) -> UserORM:
        try:
            async with self._transaction.begin():
                user = await self._user_repository.update_email(
                    user_id=user_id, email=email
                )
                if user is None:
                    raise UserNotFoundError
        except IntegrityError as error:
            raise EmailAlreadyExistsError from error

        return user

    async def delete_user(self, *, user_id: int) -> None:
        async with self._transaction.begin():
            deleted = await self._user_repository.delete_by_id(user_id)
            if not deleted:
                raise UserNotFoundError

# add     = 标记“准备写入”
# flush   = 发 SQL，检查约束，拿到生成 ID
# commit  = 正式确认，其他事务可见
# rollback = 撤销本次事务所有修改
