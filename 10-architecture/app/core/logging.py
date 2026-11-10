"""统一日志配置。业务代码通过 logging.getLogger(__name__) 获取 logger。"""

import logging

from app.core.request_context import get_request_id


class RequestIdFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = get_request_id() or "-"
        return True


def configure_logging(level: str) -> None:
    logging.basicConfig(
        level=level.upper(),
        format="%(asctime)s %(levelname)s %(name)s request_id=%(request_id)s %(message)s",
    )
    root_logger = logging.getLogger()
    for handler in root_logger.handlers:
        if not any(
            isinstance(log_filter, RequestIdFilter) for log_filter in handler.filters
        ):
            handler.addFilter(RequestIdFilter())
