"""Add archived to Tab

Revision ID: a1b2c3d4e5f6
Revises: f3a1c9d2b7e4
Create Date: 2026-09-20 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1b2c3d4e5f6'
down_revision: Union[str, Sequence[str], None] = 'f3a1c9d2b7e4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Soft-delete flag: an alternative to hard-deleting a tab (DELETE
    # /{tab_id}) that just hides it from the default "my tabs" list while
    # keeping it recoverable. server_default keeps existing rows non-null.
    op.add_column('tabs', sa.Column('archived', sa.Boolean(), nullable=False, server_default=sa.false()))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('tabs', 'archived')
