"""initial

Revision ID: f3b0d559a359
Revises:
Create Date: 2026-11-07 16:59:32.597229

"""
from typing import Sequence, Union

# revision identifiers, used by Alembic.
revision: str = "f3b0d559a359"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
