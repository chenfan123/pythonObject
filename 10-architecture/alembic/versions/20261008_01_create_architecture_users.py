"""create architecture users

Revision ID: 20261008_01
Revises:
Create Date: 2026-10-08
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op


revision: str = "20261008_01"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "architecture_users",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("email", sa.String(length=320), nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
    )
    op.create_index(
        "ix_architecture_users_email",
        "architecture_users",
        ["email"],
        unique=True,
    )


def downgrade() -> None:
    op.drop_index("ix_architecture_users_email", table_name="architecture_users")
    op.drop_table("architecture_users")
