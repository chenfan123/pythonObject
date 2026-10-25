"""create user settings

Revision ID: 20261014_01
Revises: 20261008_01
Create Date: 2026-10-14
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op


revision: str = "20261014_01"
down_revision: str | None = "20261008_01"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "architecture_user_settings",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("locale", sa.String(length=20), nullable=False),
        sa.Column(
            "email_notifications",
            sa.Boolean(),
            nullable=False,
            server_default=sa.text("true"),
        ),
        sa.ForeignKeyConstraint(["user_id"], ["architecture_users.id"], ondelete="CASCADE"),
    )
    op.create_index(
        "ix_architecture_user_settings_user_id",
        "architecture_user_settings",
        ["user_id"],
        unique=True,
    )


def downgrade() -> None:
    op.drop_index("ix_architecture_user_settings_user_id", table_name="architecture_user_settings")
    op.drop_table("architecture_user_settings")
