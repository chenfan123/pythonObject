class DomainError(Exception):
    """业务层可抛出的错误；不依赖 FastAPI 或 HTTP 状态码。"""

    code = "DOMAIN_ERROR"
    message = "A domain error occurred"


class EmailAlreadyExistsError(DomainError):
    code = "EMAIL_ALREADY_EXISTS"
    message = "Email already exists"


class UserNotFoundError(DomainError):
    code = "USER_NOT_FOUND"
    message = "User was not found"
