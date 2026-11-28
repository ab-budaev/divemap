"""spots

Revision ID: b3c8f2a1d4e7
Revises: 0124690ce392
Create Date: 2026-11-28 12:00:00.000000

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "b3c8f2a1d4e7"
down_revision: Union[str, Sequence[str], None] = "0124690ce392"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

spots_table = sa.table(
    "spots",
    sa.column("id", sa.Uuid),
    sa.column("name", sa.Text),
    sa.column("description", sa.Text),
    sa.column("lat", sa.Float),
    sa.column("lng", sa.Float),
)

DEMO_SPOTS = [
    {
        "id": "f7a3c1e8-2b4d-4e9f-8a5c-6d0b1e2f3a44",
        "name": "Байкал, Листвянка",
        "description": "Ледовые погружения, прозрачность до 40 метров.",
        "lat": 51.8461,
        "lng": 104.8722,
    },
    {
        "id": "1c9e4b7a-5d2f-4a8b-9c3e-0f1d2b4a6c88",
        "name": "Шарм-эль-Шейх, Рас Умм Сид",
        "description": "Коралловая стенка, круглый год тёплая вода.",
        "lat": 27.8667,
        "lng": 34.2974,
    },
    {
        "id": "9d2b6f1c-4a7e-4d3c-b8f5-1e0a9c6d3b22",
        "name": "Голубая дыра",
        "description": "Знаменитый карстовый провал у барьерного рифа Белиза.",
        "lat": 17.3156,
        "lng": -87.5351,
    },
]


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("spots",
    sa.Column("id", sa.Uuid(), nullable=False),
    sa.Column("name", sa.Text(), nullable=False),
    sa.Column("description", sa.Text(), nullable=True),
    sa.Column("lat", sa.Float(), nullable=False),
    sa.Column("lng", sa.Float(), nullable=False),
    sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
    sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
    sa.PrimaryKeyConstraint("id")
    )
    op.bulk_insert(spots_table, DEMO_SPOTS)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("spots")
