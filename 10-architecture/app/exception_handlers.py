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


async def handle_unexpected_error(request: Request, _error: Exception) -> JSONResponse:
    """日志由请求 Middleware 记录堆栈；客户端只获得安全且可关联的错误体。"""
    request_id = getattr(request.state, "request_id", None)
    headers = {"X-Request-ID": request_id} if request_id else None
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "code": "INTERNAL_SERVER_ERROR",
            "message": "Internal server error",
            "request_id": request_id,
        },
        headers=headers,
    )


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(DomainError, handle_domain_error)
    app.add_exception_handler(Exception, handle_unexpected_error)
