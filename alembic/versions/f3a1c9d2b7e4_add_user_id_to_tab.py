"""Add user_id to Tab

Revision ID: f3a1c9d2b7e4
Revises: 53c9271c99f3
Create Date: 2026-09-19 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f3a1c9d2b7e4'
down_revision: Union[str, Sequence[str], None] = '53c9271c99f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Plain string owner reference (no FK constraint yet — there's no real
    # auth/session system in place, just a dev-mode bypass user), so tabs
    # can be scoped to "my tabs" without hard-coupling to a FK that would
    # break once real per-user auth replaces the current dev bypass.
    op.add_column('tabs', sa.Column('user_id', sa.String(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('tabs', 'user_id')
