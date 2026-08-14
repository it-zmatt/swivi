from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/days", tags=["days"])


@router.get("", response_model=list[schemas.DayOut])
def get_days(db: Session = Depends(get_db)):
    return crud.list_days(db)
