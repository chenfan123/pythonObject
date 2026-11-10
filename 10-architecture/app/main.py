from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import get_settings
from app.core.logging import configure_logging
from app.db.session import engine
from app.exception_handlers import register_exception_handlers
from app.middleware.request_logging import register_request_logging
from app.routers.users import router as users_router


@asynccontextmanager  # 异步上下文管理器
async def lifespan(app: FastAPI):  # 生命周期管理器
    yield
    await engine.dispose()  # 关闭数据库连接


settings = get_settings()
configure_logging(settings.log_level)

app = FastAPI(title="Architecture Learning Lab",
              lifespan=lifespan)  # 创建FastAPI应用
register_request_logging(app)
register_exception_handlers(app)  # 注册异常处理器
app.include_router(users_router)  # 包含用户路由


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
