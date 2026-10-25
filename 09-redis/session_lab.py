"""Redis Session 教学实验：登录、当前用户、注销。"""

from contextlib import asynccontextmanager
from typing import Annotated
from uuid import uuid4

import redis.asyncio as redis
from fastapi import Cookie, Depends, FastAPI, HTTPException, Request, Response, status
from pydantic import BaseModel, Field


REDIS_URL = "redis://localhost:6380/0"
SESSION_TTL_SECONDS = 1800
COOKIE_NAME = "session_id"


class LoginDTO(BaseModel):
    """教学用登录输入；真实项目还要验证密码。"""

    username: str = Field(min_length=1, max_length=50)


class CurrentUserDTO(BaseModel):
    id: int
    username: str
    role: str


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = redis.from_url(REDIS_URL, decode_responses=True)
    await client.ping()
    app.state.redis = client
    try:
        yield
    finally:
        await client.aclose()


app = FastAPI(title="Redis Session Lab", lifespan=lifespan)


def session_key(session_id: str) -> str:
    return f"session:lab:{session_id}"


async def get_current_user(
    request: Request,
    session_id: Annotated[str | None, Cookie()] = None,
) -> CurrentUserDTO:
    """认证 Dependency：缺 Cookie 或 Redis Session 均视为未登录。"""
    if session_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not logged in")

    data = await request.app.state.redis.hgetall(session_key(session_id))
    if not data:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Session expired or revoked")
    return CurrentUserDTO(id=int(data["user_id"]), username=data["username"], role=data["role"])


@app.post("/lab/session/login", response_model=CurrentUserDTO)
async def login(payload: LoginDTO, request: Request, response: Response) -> CurrentUserDTO:
    # 仅为演示固定身份；真实项目此处先验证账号和密码。
    user = CurrentUserDTO(id=42, username=payload.username, role="member")
    session_id = str(uuid4())
    await request.app.state.redis.hset(
        session_key(session_id),
        mapping={"user_id": user.id, "username": user.username, "role": user.role},
    )
    await request.app.state.redis.expire(session_key(session_id), SESSION_TTL_SECONDS)

    response.set_cookie(
        key=COOKIE_NAME,
        value=session_id,
        max_age=SESSION_TTL_SECONDS,
        httponly=True,
        samesite="lax",
        # 本地 HTTP 实验必须为 False；生产 HTTPS 必须为 True。
        secure=False,
    )
    return user


@app.get("/lab/session/me", response_model=CurrentUserDTO)
async def me(current_user: Annotated[CurrentUserDTO, Depends(get_current_user)]) -> CurrentUserDTO:
    return current_user


@app.post("/lab/session/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(
    request: Request,
    response: Response,
    session_id: Annotated[str | None, Cookie()] = None,
) -> None:
    if session_id is not None:
        await request.app.state.redis.delete(session_key(session_id))
    response.delete_cookie(COOKIE_NAME)
    # 204 不能携带响应体；Cookie 删除头仍写入当前 Response。
    response.status_code = status.HTTP_204_NO_CONTENT
