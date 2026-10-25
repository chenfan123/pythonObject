from sqlalchemy import delete, func, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import UserORM

# 将 SQLAlchemy 查询细节封装起来


class UserRepository:
    """只处理 UserORM 的数据库读写，不处理 HTTP 或业务状态码。"""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_email(self, email: str) -> UserORM | None:
        # select(UserORM).where(UserORM.email == email) → 构建 SQL 查询对象
        statement = select(UserORM).where(UserORM.email == email)
        # result = await session.execute(statement) -> 执行 SQL 查询，返回结果集
        # result.scalar() -> 返回单个值，而不是结果集
        return await self._session.scalar(statement)

    async def get_by_id(self, user_id: int) -> UserORM | None:
        """主键查询由 Repository 封装，调用方不接触 SQLAlchemy Session。"""
        return await self._session.get(UserORM, user_id)

    @staticmethod
    def _conditions_for(
        *, keyword: str | None, email_domain: str | None
    ) -> list:
        """构建可复用于列表与计数查询的 SQL 筛选表达式。"""
        conditions = []
        if keyword is not None:
            conditions.append(UserORM.email.ilike(f"%{keyword}%"))
        if email_domain is not None:
            conditions.append(UserORM.email.ilike(f"%@{email_domain}"))
        return conditions

    async def list(
        self,
        *,
        keyword: str | None,
        email_domain: str | None,
        offset: int,
        limit: int,
    ) -> list[UserORM]:
        """以稳定主键顺序读取一页用户。"""
        conditions = self._conditions_for(
            keyword=keyword, email_domain=email_domain
        )
        statement = (
            select(UserORM)
            .where(*conditions)
            .order_by(UserORM.id.asc())
            .offset(offset)
            .limit(limit)
        )
        result = await self._session.execute(statement)
        return list(result.scalars().all())

    async def count(self, *, keyword: str | None, email_domain: str | None) -> int:
        """返回当前列表筛选条件下的用户总数。"""
        conditions = self._conditions_for(
            keyword=keyword, email_domain=email_domain
        )
        statement = select(func.count()).select_from(
            UserORM).where(*conditions)
        return await self._session.scalar(statement) or 0

    async def update_email(self, *, user_id: int, email: str) -> UserORM | None:
        """更新邮箱并返回更新后的记录；没有匹配用户时返回 None。"""
        statement = (
            update(UserORM)
            .where(UserORM.id == user_id)
            .values(email=email)
            .returning(UserORM)
        )
        # returning 匹配到用户并更新 → 直接拿到更新后的 ORM 对象；没有的话返回None
        result = await self._session.execute(statement)
        return result.scalar_one_or_none()

    async def delete_by_id(self, user_id: int) -> bool:
        """删除目标用户；没有匹配记录时返回 False。"""
        statement = delete(UserORM).where(UserORM.id == user_id)
        result = await self._session.execute(statement)
        return result.rowcount == 1

    def add(self, user: UserORM) -> None:
        self._session.add(user)
