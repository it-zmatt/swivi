import datetime

from sqlalchemy.orm import Session

from app import models, schemas


# ---------- Days / TimeSlots (read-only lookups) ----------
def list_days(db: Session):
    return db.query(models.Day).order_by(models.Day.sort_order).all()


def list_time_slots(db: Session):
    return db.query(models.TimeSlot).order_by(models.TimeSlot.sort_order).all()


# ---------- Weeks ----------
def get_week(db: Session, week_id: str):
    return db.query(models.Week).filter(models.Week.id == week_id).first()


def list_weeks(db: Session):
    return db.query(models.Week).order_by(models.Week.start_date).all()


def create_week(db: Session, week_in: schemas.WeekCreate, year: int | None = None) -> models.Week:
    year = year or datetime.date.today().year
    month, day = int(week_in.id[:2]), int(week_in.id[2:])
    start_date = datetime.date(year, month, day)
    end_date = start_date + datetime.timedelta(days=4)

    week = models.Week(id=week_in.id, start_date=start_date, end_date=end_date)
    db.add(week)
    db.commit()
    db.refresh(week)
    return week


def delete_week(db: Session, week: models.Week) -> None:
    db.delete(week)
    db.commit()


# ---------- Tasks ----------
def get_task(db: Session, task_id: str):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def list_tasks(db: Session, week_id: str | None = None, day_id: str | None = None):
    query = db.query(models.Task)
    if week_id:
        query = query.filter(models.Task.week_id == week_id)
    if day_id:
        query = query.filter(models.Task.day_id == day_id)
    return query.order_by(models.Task.week_id, models.Task.day_id, models.Task.time_id).all()


def create_task(db: Session, task_in: schemas.TaskCreate) -> models.Task:
    task_id = models.make_task_id(task_in.week_id, task_in.day_id, task_in.time_id)
    task = models.Task(
        id=task_id,
        week_id=task_in.week_id,
        day_id=task_in.day_id,
        time_id=task_in.time_id,
        task_type=task_in.task_type,
        ticket=task_in.ticket,
        description=task_in.description,
        request=task_in.request,
        site=task_in.site,
        access_notes=task_in.access_notes,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def update_task(db: Session, task: models.Task, task_in: schemas.TaskUpdate) -> models.Task:
    for field, value in task_in.model_dump(exclude_unset=True).items():
        setattr(task, field, value)
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task: models.Task) -> None:
    db.delete(task)
    db.commit()
