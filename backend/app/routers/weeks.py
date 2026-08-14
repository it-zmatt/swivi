from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db
from app.models import make_task_id

router = APIRouter(prefix="/weeks", tags=["weeks"])


@router.get("", response_model=list[schemas.WeekOut])
def get_weeks(db: Session = Depends(get_db)):
    return crud.list_weeks(db)


@router.post("", response_model=schemas.WeekOut, status_code=status.HTTP_201_CREATED)
def create_week(week_in: schemas.WeekCreate, db: Session = Depends(get_db)):
    if crud.get_week(db, week_in.id):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Week '{week_in.id}' already exists")
    return crud.create_week(db, week_in)


@router.get("/{week_id}", response_model=schemas.WeekOut)
def get_week(week_id: str, db: Session = Depends(get_db)):
    week = crud.get_week(db, week_id)
    if not week:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Week '{week_id}' not found")
    return week


@router.delete("/{week_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_week(week_id: str, db: Session = Depends(get_db)):
    week = crud.get_week(db, week_id)
    if not week:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Week '{week_id}' not found")
    crud.delete_week(db, week)


@router.get("/{week_id}/grid", response_model=schemas.WeekGrid)
def get_week_grid(week_id: str, db: Session = Depends(get_db)):
    week = crud.get_week(db, week_id)
    if not week:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Week '{week_id}' not found")

    days = crud.list_days(db)
    time_slots = crud.list_time_slots(db)
    tasks = {task.id: task for task in crud.list_tasks(db, week_id=week_id)}

    cells = []
    for day in days:
        for slot in time_slots:
            task = tasks.get(make_task_id(week_id, day.id, slot.id))
            cells.append(schemas.GridCell(day_id=day.id, time_id=slot.id, task=task))

    return schemas.WeekGrid(week=week, days=days, time_slots=time_slots, cells=cells)
