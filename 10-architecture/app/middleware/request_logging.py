"""不记录敏感内容的请求关联与访问日志。"""

import logging
from collections.abc import Awaitable, Callable
from time import perf_counter
from uuid import uuid4

from fastapi import FastAPI, Request, Response

from app.core.request_context import reset_request_id, set_request_id


logger = logging.getLogger(__name__)
RequestHandler = Callable[[Request], Awaitable[Response]]


def register_request_logging(app: FastAPI) -> None:
    @app.middleware("http")
    async def log_request(request: Request, call_next: RequestHandler) -> Response:
        request_id = request.headers.get("X-Request-ID") or str(uuid4())
        request.state.request_id = request_id
        context_token = set_request_id(request_id)
        started_at = perf_counter()

        try:
            response = await call_next(request)
            duration_ms = round((perf_counter() - started_at) * 1_000, 2)
            response.headers["X-Request-ID"] = request_id
            logger.info(
                "request completed request_id=%s method=%s path=%s status=%s duration_ms=%s",
                request_id,
                request.method,
                request.url.path,
                response.status_code,
                duration_ms,
            )
            return response
        except Exception:
            duration_ms = round((perf_counter() - started_at) * 1_000, 2)
            logger.exception(
                "request failed request_id=%s method=%s path=%s duration_ms=%s",
                request_id,
                request.method,
                request.url.path,
                duration_ms,
            )
            raise
        finally:
            reset_request_id(context_token)
