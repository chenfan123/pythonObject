from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db_session
from app.repositories.user_repository import UserRepository
from app.repositories.user_settings_repository import UserSettingsRepository
from app.services.user_service import UserService


def get_user_service(
    session: Annotated[AsyncSession, Depends(get_db_session)],
) -> UserService:
    """为一次 HTTP 请求装配共享同一 Session 的用户服务。"""
    return UserService(
        UserRepository(session),
        UserSettingsRepository(session),
        session,
    )
