from itertools import count

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field


app = FastAPI(
    title="FastAPI CRUD Learning Project",
    description="An in-memory CRUD API used to learn FastAPI and OpenAPI.",
    version="0.1.0",
)


class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    email: str = Field(min_length=3, max_length=200)
    password: str = Field(min_length=8)


class UserUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=50)
    email: str | None = Field(default=None, min_length=3, max_length=200)


class UserResponse(BaseModel):
    id: int
    name: str
    email: str


users: dict[int, UserResponse] = {}
user_ids = count(start=1)


def find_user_or_404(user_id: int) -> UserResponse:
    user = users.get(user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "code": "USER_NOT_FOUND",
                "message": f"User {user_id} was not found",
            },
        )

    return user


def ensure_email_available(email: str, *, excluded_user_id: int | None = None) -> None:
    email_is_used = any(
        user.email == email and user.id != excluded_user_id
        for user in users.values()
    )

    if email_is_used:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={
                "code": "EMAIL_ALREADY_EXISTS",
                "message": "Email is already registered",
            },
        )


@app.get(
    "/health",
    tags=["System"],
    summary="Check service health",
)
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get(
    "/users",
    response_model=list[UserResponse],
    tags=["Users"],
    summary="List users",
)
async def list_users() -> list[UserResponse]:
    return list(users.values())


@app.post(
    "/users",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Users"],
    summary="Create a user",
    responses={409: {"description": "Email already exists"}},
)
async def create_user(payload: UserCreate) -> UserResponse:
    ensure_email_available(payload.email)

    user = UserResponse(
        id=next(user_ids),
        name=payload.name,
        email=payload.email,
    )
    users[user.id] = user
    return user


@app.get(
    "/users/{user_id}",
    response_model=UserResponse,
    tags=["Users"],
    summary="Get a user",
    responses={404: {"description": "User not found"}},
)
async def get_user(user_id: int) -> UserResponse:
    return find_user_or_404(user_id)


@app.patch(
    "/users/{user_id}",
    response_model=UserResponse,
    tags=["Users"],
    summary="Partially update a user",
    responses={
        404: {"description": "User not found"},
        409: {"description": "Email already exists"},
    },
)
async def update_user(user_id: int, payload: UserUpdate) -> UserResponse:
    user = find_user_or_404(user_id)
    # exclude_unset=True 只保留客户端实际传入的字段。
    changes = payload.model_dump(exclude_unset=True)

    if "email" in changes and changes["email"] is not None:
        ensure_email_available(changes["email"], excluded_user_id=user_id)

    updated_user = user.model_copy(update=changes)
    users[user_id] = updated_user
    return updated_user


@app.delete(
    "/users/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Users"],
    summary="Delete a user",
    responses={404: {"description": "User not found"}},
)
async def delete_user(user_id: int) -> Response:
    find_user_or_404(user_id)
    del users[user_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
