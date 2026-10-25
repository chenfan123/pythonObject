from typing import Annotated

from fastapi import APIRouter, Depends, Query, Response, status

from app.dependencies.users import get_user_service
from app.schemas.user import (
    UserCreateDTO,
    UserEmailUpdateDTO,
    UserPageDTO,
    UserResponseDTO,
)
from app.services.user_service import UserService


router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=UserPageDTO)
async def list_users(
    service: Annotated[UserService, Depends(get_user_service)],
    keyword: Annotated[str | None, Query(min_length=1, max_length=100)] = None,
    email_domain: Annotated[str | None, Query(min_length=3, max_length=253)] = None,
    offset: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=100)] = 20,
) -> UserPageDTO:
    users, total = await service.list_users(
        keyword=keyword,
        email_domain=email_domain,
        offset=offset,
        limit=limit,
    )
    return UserPageDTO(
        items=[UserResponseDTO.model_validate(user) for user in users],
        total=total,
        offset=offset,
        limit=limit,
    )


@router.get("/{user_id}", response_model=UserResponseDTO)
async def get_user(
    user_id: int,
    service: Annotated[UserService, Depends(get_user_service)],
) -> UserResponseDTO:
    user = await service.get_user(user_id)
    return UserResponseDTO.model_validate(user)


@router.patch(
    "/{user_id}",
    response_model=UserResponseDTO,
    responses={
        status.HTTP_409_CONFLICT: {
            "description": "Email already exists",
        },
    },
)
async def update_user_email(
    user_id: int,
    payload: UserEmailUpdateDTO,
    service: Annotated[UserService, Depends(get_user_service)],
) -> UserResponseDTO:
    user = await service.update_user_email(user_id=user_id, email=payload.email)
    return UserResponseDTO.model_validate(user)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
    service: Annotated[UserService, Depends(get_user_service)],
) -> Response:
    await service.delete_user(user_id=user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponseDTO,
    responses={
        status.HTTP_409_CONFLICT: {
            "description": "Email already exists",
            "content": {
                "application/json": {
                    "example": {
                        "code": "EMAIL_ALREADY_EXISTS",
                        "message": "Email already exists",
                    }
                }
            },
        }
    },
)
async def create_user(
    payload: UserCreateDTO,
    service: Annotated[UserService, Depends(get_user_service)],
) -> UserResponseDTO:
    user = await service.create_user(email=payload.email, password=payload.password)
    return UserResponseDTO.model_validate(user)
