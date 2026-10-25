from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base

# architecture_users 表在 Python 中的映射


class UserORM(Base):
    """数据库模型：只描述 architecture_users 表如何映射为 Python 对象。"""

    __tablename__ = "architecture_users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(320), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
