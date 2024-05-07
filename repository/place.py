from sqlalchemy import func
from sqlalchemy.orm import Session
from random import randint

from schemas import Place
import models
from core.geolocator import *
from logger_conf import logger


def insert(place: str, db: Session):
    address_details = get_coordinates(place)
    db_id = randint(1, 9999999)

    try:
        place = models.Place(id=db_id,
                             name=place,
                             address=address_details.address,
                             latitude=address_details.latitude,
                             longitude=address_details.longitude)
        db.add(place)
        db.commit()
        db.refresh(place)
        return place
    except Exception:
        logger.error(f"Error inserting data", exc_info=True)
        db.rollback()
        return None


def delete(id: int, db: Session):
    address_id = db.query(Place).filter(Place.id == id).first()
    if address_id is None:
        return {"message": f"No record found for address id {id}"}
    try:
        db.delete(address_id)
        db.commit()
        return {"message": f"Successfully deleted address id {id}"}
    except Exception:
        logger.error(f"Database issue", exc_info=True)
        db.rollback()
        return {"message": f"Database issue"}

