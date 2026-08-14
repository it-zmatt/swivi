"""seed fixed days and time_slots lookup data

Revision ID: 61ce62cf15d1
Revises: 36b53d7968bc
Create Date: 2026-08-14 16:00:46.943280

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '61ce62cf15d1'
down_revision: Union[str, None] = '36b53d7968bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


days_table = sa.table(
    "days",
    sa.column("id", sa.String),
    sa.column("name", sa.String),
    sa.column("sort_order", sa.Integer),
)

time_slots_table = sa.table(
    "time_slots",
    sa.column("id", sa.String),
    sa.column("start_time", sa.String),
    sa.column("end_time", sa.String),
    sa.column("label", sa.String),
    sa.column("sort_order", sa.Integer),
)

DAYS = [
    {"id": "MON", "name": "Monday", "sort_order": 1},
    {"id": "TUE", "name": "Tuesday", "sort_order": 2},
    {"id": "WED", "name": "Wednesday", "sort_order": 3},
    {"id": "THU", "name": "Thursday", "sort_order": 4},
    {"id": "FRI", "name": "Friday", "sort_order": 5},
]

# 8 one-hour slots covering 8:00 AM - 4:00 PM
TIME_SLOTS = [
    {"id": "08", "start_time": "08:00", "end_time": "09:00", "label": "8:00 AM - 9:00 AM", "sort_order": 1},
    {"id": "09", "start_time": "09:00", "end_time": "10:00", "label": "9:00 AM - 10:00 AM", "sort_order": 2},
    {"id": "10", "start_time": "10:00", "end_time": "11:00", "label": "10:00 AM - 11:00 AM", "sort_order": 3},
    {"id": "11", "start_time": "11:00", "end_time": "12:00", "label": "11:00 AM - 12:00 PM", "sort_order": 4},
    {"id": "12", "start_time": "12:00", "end_time": "13:00", "label": "12:00 PM - 1:00 PM", "sort_order": 5},
    {"id": "13", "start_time": "13:00", "end_time": "14:00", "label": "1:00 PM - 2:00 PM", "sort_order": 6},
    {"id": "14", "start_time": "14:00", "end_time": "15:00", "label": "2:00 PM - 3:00 PM", "sort_order": 7},
    {"id": "15", "start_time": "15:00", "end_time": "16:00", "label": "3:00 PM - 4:00 PM", "sort_order": 8},
]


def upgrade() -> None:
    op.bulk_insert(days_table, DAYS)
    op.bulk_insert(time_slots_table, TIME_SLOTS)


def downgrade() -> None:
    op.execute(time_slots_table.delete())
    op.execute(days_table.delete())
