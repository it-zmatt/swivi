from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db
from app.models import make_task_id

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("", response_model=list[schemas.TaskOut])
def get_tasks(
    week_id: str | None = None,
    day_id: str | None = None,
    db: Session = Depends(get_db),
):
    return crud.list_tasks(db, week_id=week_id, day_id=day_id)


@router.post("", response_model=schemas.TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(task_in: schemas.TaskCreate, db: Session = Depends(get_db)):
    if not crud.get_week(db, task_in.week_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Week '{task_in.week_id}' not found"
        )

    task_id = make_task_id(task_in.week_id, task_in.day_id, task_in.time_id)
    if crud.get_task(db, task_id):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Task '{task_id}' already exists for this week/day/time slot",
        )

    return crud.create_task(db, task_in)


@router.get("/{task_id}", response_model=schemas.TaskOut)
def get_task(task_id: str, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task '{task_id}' not found")
    return task


@router.put("/{task_id}", response_model=schemas.TaskOut)
def update_task(task_id: str, task_in: schemas.TaskUpdate, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task '{task_id}' not found")
    return crud.update_task(db, task, task_in)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: str, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task '{task_id}' not found")
    crud.delete_task(db, task)
