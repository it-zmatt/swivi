import datetime
import re
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

WEEK_ID_PATTERN = re.compile(r"^\d{4}$")  # MMDD
DAY_ID_PATTERN = re.compile(r"^(MON|TUE|WED|THU|FRI)$")
TIME_ID_PATTERN = re.compile(r"^(0[8-9]|1[0-5])$")  # 08-15


# ---------- Day ----------
class DayOut(BaseModel):
    id: str
    name: str
    sort_order: int

    model_config = ConfigDict(from_attributes=True)


# ---------- TimeSlot ----------
class TimeSlotOut(BaseModel):
    id: str
    start_time: str
    end_time: str
    label: str
    sort_order: int

    model_config = ConfigDict(from_attributes=True)


# ---------- Week ----------
class WeekCreate(BaseModel):
    id: str = Field(..., description="Week identifier in MMDD format, e.g. '0811'")

    @field_validator("id")
    @classmethod
    def validate_week_id(cls, v: str) -> str:
        if not WEEK_ID_PATTERN.match(v):
            raise ValueError("Week id must be exactly 4 digits in MMDD format, e.g. '0811'")
        month, day = int(v[:2]), int(v[2:])
        if not (1 <= month <= 12):
            raise ValueError("Week id month must be between 01 and 12")
        if not (1 <= day <= 31):
            raise ValueError("Week id day must be between 01 and 31")
        return v


class WeekOut(BaseModel):
    id: str
    start_date: datetime.date
    end_date: datetime.date
    created_at: datetime.datetime

    model_config = ConfigDict(from_attributes=True)


# ---------- Task ----------
class TaskBase(BaseModel):
    task_type: Optional[str] = Field(None, max_length=50)
    ticket: Optional[str] = Field(None, max_length=100)
    description: Optional[str] = Field(None, max_length=1000)
    request: Optional[str] = Field(None, max_length=1000)
    site: Optional[str] = Field(None, max_length=100)
    access_notes: Optional[str] = Field(None, max_length=1000)


class TaskCreate(TaskBase):
    week_id: str
    day_id: str
    time_id: str

    @field_validator("week_id")
    @classmethod
    def validate_week_id(cls, v: str) -> str:
        if not WEEK_ID_PATTERN.match(v):
            raise ValueError("week_id must be 4 digits in MMDD format, e.g. '0811'")
        return v

    @field_validator("day_id")
    @classmethod
    def validate_day_id(cls, v: str) -> str:
        v = v.upper()
        if not DAY_ID_PATTERN.match(v):
            raise ValueError("day_id must be one of MON, TUE, WED, THU, FRI")
        return v

    @field_validator("time_id")
    @classmethod
    def validate_time_id(cls, v: str) -> str:
        v = v.zfill(2)
        if not TIME_ID_PATTERN.match(v):
            raise ValueError("time_id must be one of 08-15 (slot start hour, 8am-4pm)")
        return v


class TaskUpdate(TaskBase):
    pass


class TaskOut(TaskBase):
    id: str
    week_id: str
    day_id: str
    time_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

    model_config = ConfigDict(from_attributes=True)


# ---------- Grid (week view) ----------
class GridCell(BaseModel):
    day_id: str
    time_id: str
    task: Optional[TaskOut] = None


class WeekGrid(BaseModel):
    week: WeekOut
    days: list[DayOut]
    time_slots: list[TimeSlotOut]
    cells: list[GridCell]
