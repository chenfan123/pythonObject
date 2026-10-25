from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.core.domain_errors import (
    DomainError,
    EmailAlreadyExistsError,
    UserNotFoundError,
)


def domain_error_status_code(error: DomainError) -> int:
    """HTTP 映射属于接口边缘层，而非 Service。"""
    if isinstance(error, EmailAlreadyExistsError):
        return status.HTTP_409_CONFLICT
    if isinstance(error, UserNotFoundError):
        return status.HTTP_404_NOT_FOUND
    return status.HTTP_400_BAD_REQUEST


async def handle_domain_error(_request: Request, error: DomainError) -> JSONResponse:
    return JSONResponse(
        status_code=domain_error_status_code(error),
        content={"code": error.code, "message": error.message},
    )


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(DomainError, handle_domain_error)
