import asyncio
from uuid import uuid4

import pytest
from sqlalchemy import delete, func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from app.models.user import UserORM
from app.models.user_settings import UserSettingsORM


pytestmark = pytest.mark.integration


@pytest.mark.asyncio
async def test_concurrent_duplicate_inserts_allow_exactly_one_user(
    integration_engine: AsyncEngine,
) -> None:
    """模拟两个独立请求同时注册同一邮箱，验证数据库最终裁决唯一性。"""
    email = f"concurrent-{uuid4()}@example.com"
    start_barrier = asyncio.Barrier(2)

    async def attempt_insert() -> bool:
        async with AsyncSession(integration_engine, expire_on_commit=False) as session:
            await start_barrier.wait()
            try:
                async with session.begin():
                    session.add(UserORM(email=email, password_hash="test-hash"))
                    await session.flush()
                return True
            except IntegrityError:
                return False

    try:
        results = await asyncio.gather(attempt_insert(), attempt_insert())

        assert results.count(True) == 1
        assert results.count(False) == 1

        async with AsyncSession(integration_engine) as session:
            count = await session.scalar(
                select(func.count()).select_from(UserORM).where(UserORM.email == email)
            )
        assert count == 1
    finally:
        async with AsyncSession(integration_engine) as session:
            async with session.begin():
                await session.execute(delete(UserORM).where(UserORM.email == email))


@pytest.mark.asyncio
async def test_database_unique_email_rejects_duplicate_insert(
    integration_session: AsyncSession,
) -> None:
    """直接写 ORM，证明 UNIQUE 是数据库约束而非 Service 预检查的副作用。"""
    email = f"integration-{uuid4()}@example.com"

    integration_session.add(UserORM(email=email, password_hash="first-hash"))
    await integration_session.flush()

    with pytest.raises(IntegrityError):
        async with integration_session.begin_nested():
            integration_session.add(UserORM(email=email, password_hash="second-hash"))
            await integration_session.flush()


@pytest.mark.asyncio
async def test_deleting_user_cascades_to_user_settings(
    integration_session: AsyncSession,
) -> None:
    """验证 PostgreSQL 外键，而非只验证 ORM 或迁移文件写法。"""
    email = f"cascade-{uuid4()}@example.com"
    user = UserORM(email=email, password_hash="test-hash")
    integration_session.add(user)
    await integration_session.flush()

    settings = UserSettingsORM(user_id=user.id)
    integration_session.add(settings)
    await integration_session.flush()
    settings_id = settings.id

    await integration_session.execute(delete(UserORM).where(UserORM.id == user.id))

    # 数据库已级联删除；清除当前 Session 的旧对象缓存后再验证真实存储状态。
    integration_session.expire_all()
    assert await integration_session.get(UserSettingsORM, settings_id) is None
