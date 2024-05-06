from sqlalchemy import func
from sqlalchemy.orm import Session

from schemas import Place
from data_store import models
import schemas

def get_max_id(db:Session):
    return db.query(func.max(Place.id)).scalar()

def insert_place(request: Place, db: Session):
    new_place = models.Place()