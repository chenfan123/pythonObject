"""应用配置：统一从环境变量读取，并在启动阶段完成校验。"""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    database_url: str
    log_level: str = "INFO"
    max_page_size: int = Field(default=100, ge=1, le=1_000)


@lru_cache
def get_settings() -> Settings:
    """配置在一个进程内只构造一次，避免各处重复读取环境变量。"""
    return Settings()
