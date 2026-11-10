import os
from collections.abc import AsyncIterator

import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)


@pytest.fixture(scope="session")
def integration_database_url() -> str:
    database_url = os.getenv("INTEGRATION_DATABASE_URL")
    if database_url is None:
        pytest.skip("Set INTEGRATION_DATABASE_URL to run PostgreSQL integration tests")
    return database_url


@pytest_asyncio.fixture
async def integration_engine(integration_database_url: str) -> AsyncIterator[AsyncEngine]:
    # pytest-asyncio 默认每个测试函数使用独立事件循环；Engine 也保持同一生命周期。
    engine = create_async_engine(integration_database_url)
    try:
        yield engine
    finally:
        await engine.dispose()


@pytest_asyncio.fixture
async def integration_session(
    integration_engine: AsyncEngine,
) -> AsyncIterator[AsyncSession]:
    """一个测试绑定一条连接和外层事务；结束时回滚全部测试数据。"""
    async with integration_engine.connect() as connection:
        outer_transaction = await connection.begin()
        session = AsyncSession(
            bind=connection,
            expire_on_commit=False,
            join_transaction_mode="create_savepoint",
        )
        try:
            yield session
        finally:
            await session.close()
            await outer_transaction.rollback()
