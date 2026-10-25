from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user_settings import UserSettingsORM


class UserSettingsRepository:
    """只负责 user settings 表的读写，不提交事务。"""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    def add_default_for_user(self, user_id: int) -> None:
        self._session.add(UserSettingsORM(user_id=user_id))
