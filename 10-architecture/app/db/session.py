import os
from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


def get_database_url() -> str:
    """配置属于基础设施：源码不保存真实连接密码。"""
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise RuntimeError("DATABASE_URL is required")
    return database_url


# 创建异步引擎:Engine → 应用级数据库连接与连接池管理器
engine = create_async_engine(get_database_url(), echo=True)
SessionFactory = async_sessionmaker(engine, expire_on_commit=False)


# 创建异步会话工厂,用于获取数据库会话
async def get_db_session() -> AsyncIterator[AsyncSession]:
    """每个请求获得一个 Session，并在请求结束后关闭。"""
    async with SessionFactory() as session:  # 创建Session
        yield session  # 返回一个异步迭代器,把 session 交给路由用
