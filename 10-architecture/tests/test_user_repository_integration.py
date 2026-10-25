import os
from uuid import uuid4

import pytest
from sqlalchemy import delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.models.user import UserORM
from app.models.user_settings import UserSettingsORM


@pytest.mark.asyncio
@pytest.mark.integration
async def test_database_unique_email_rejects_duplicate_insert() -> None:
    """直接写 ORM，证明 UNIQUE 是数据库约束而非 Service 预检查的副作用。"""
    database_url = os.getenv("INTEGRATION_DATABASE_URL")
    if database_url is None:
        pytest.skip("Set INTEGRATION_DATABASE_URL to run PostgreSQL integration tests")

    engine = create_async_engine(database_url)
    session_factory = async_sessionmaker(engine, expire_on_commit=False)
    email = f"integration-{uuid4()}@example.com"

    try:
        async with session_factory() as session:
            async with session.begin():
                session.add(UserORM(email=email, password_hash="first-hash"))

        async with session_factory() as session:
            with pytest.raises(IntegrityError):
                async with session.begin():
                    session.add(UserORM(email=email, password_hash="second-hash"))
                    await session.flush()
    finally:
        async with session_factory() as session:
            async with session.begin():
                await session.execute(delete(UserORM).where(UserORM.email == email))
        await engine.dispose()


@pytest.mark.asyncio
@pytest.mark.integration
async def test_deleting_user_cascades_to_user_settings() -> None:
    """验证 PostgreSQL 外键，而非只验证 ORM 或迁移文件写法。"""
    database_url = os.getenv("INTEGRATION_DATABASE_URL")
    if database_url is None:
        pytest.skip("Set INTEGRATION_DATABASE_URL to run PostgreSQL integration tests")

    engine = create_async_engine(database_url)
    session_factory = async_sessionmaker(engine, expire_on_commit=False)
    email = f"cascade-{uuid4()}@example.com"
    user_id: int | None = None
    settings_id: int | None = None

    try:
        async with session_factory() as session:
            async with session.begin():
                user = UserORM(email=email, password_hash="test-hash")
                session.add(user)
                await session.flush()
                user_id = user.id

                settings = UserSettingsORM(user_id=user.id)
                session.add(settings)
                await session.flush()
                settings_id = settings.id

        async with session_factory() as session:
            async with session.begin():
                await session.execute(delete(UserORM).where(UserORM.id == user_id))

        async with session_factory() as session:
            assert await session.get(UserSettingsORM, settings_id) is None
    finally:
        async with session_factory() as session:
            async with session.begin():
                await session.execute(delete(UserORM).where(UserORM.email == email))
        await engine.dispose()
