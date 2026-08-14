import datetime

from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.database import Base


class Day(Base):
    """Fixed lookup table: Monday - Friday only."""

    __tablename__ = "days"

    id = Column(String(3), primary_key=True)  # MON, TUE, WED, THU, FRI
    name = Column(String(20), nullable=False)  # Monday, Tuesday, ...
    sort_order = Column(Integer, nullable=False)  # 1-5

    tasks = relationship("Task", back_populates="day")


class TimeSlot(Base):
    """Fixed lookup table: 8 one-hour slots covering 8am - 4pm."""

    __tablename__ = "time_slots"

    id = Column(String(2), primary_key=True)  # 08, 09, 10, 11, 12, 13, 14, 15 (slot start hour, 24h)
    start_time = Column(String(5), nullable=False)  # "08:00"
    end_time = Column(String(5), nullable=False)  # "09:00"
    label = Column(String(20), nullable=False)  # "8:00 AM - 9:00 AM"
    sort_order = Column(Integer, nullable=False)  # 1-8

    tasks = relationship("Task", back_populates="time_slot")


class Week(Base):
    """A week is identified by its Monday's date in MMDD format, e.g. '0811'."""

    __tablename__ = "weeks"

    id = Column(String(4), primary_key=True)  # MMDD, e.g. "0811"
    start_date = Column(Date, nullable=False)  # Monday of the week
    end_date = Column(Date, nullable=False)  # Friday of the week
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    tasks = relationship("Task", back_populates="week", cascade="all, delete-orphan")


class Task(Base):
    """
    One task per (week, day, time slot) cell.

    Primary key is composed as WID_DID_TID, e.g. "0811_MON_08"
    (week id "0811" + day id "MON" + time slot id "08").
    """

    __tablename__ = "tasks"
    __table_args__ = (
        UniqueConstraint("week_id", "day_id", "time_id", name="uq_tasks_week_day_time"),
    )

    id = Column(String(16), primary_key=True)  # WID_DID_TID

    week_id = Column(String(4), ForeignKey("weeks.id", ondelete="CASCADE"), nullable=False)
    day_id = Column(String(3), ForeignKey("days.id"), nullable=False)
    time_id = Column(String(2), ForeignKey("time_slots.id"), nullable=False)

    task_type = Column(String(50), nullable=True)
    ticket = Column(String(100), nullable=True)
    description = Column(String(1000), nullable=True)
    request = Column(String(1000), nullable=True)
    site = Column(String(100), nullable=True)
    access_notes = Column(String(1000), nullable=True)

    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow, nullable=False
    )

    week = relationship("Week", back_populates="tasks")
    day = relationship("Day", back_populates="tasks")
    time_slot = relationship("TimeSlot", back_populates="tasks")


def make_task_id(week_id: str, day_id: str, time_id: str) -> str:
    return f"{week_id}_{day_id}_{time_id}"
