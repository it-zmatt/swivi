from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/timeslots", tags=["timeslots"])


@router.get("", response_model=list[schemas.TimeSlotOut])
def get_time_slots(db: Session = Depends(get_db)):
    return crud.list_time_slots(db)
