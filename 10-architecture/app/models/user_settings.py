from sqlalchemy import Boolean, ForeignKey, String, text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class UserSettingsORM(Base):
    """每个用户一份默认设置，用于演示跨 Repository 的同一事务。"""

    __tablename__ = "architecture_user_settings"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("architecture_users.id", ondelete="CASCADE"),
        unique=True,
        index=True,
    )
    locale: Mapped[str] = mapped_column(String(20), default="zh-CN")
    email_notifications: Mapped[bool] = mapped_column(
        Boolean,
        server_default=text("true"),
    )
