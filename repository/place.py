from sqlalchemy import func
from sqlalchemy.orm import Session
from random import randint

from schemas import *
import models
from core.geolocator import *
from logger_conf import logger


def get_all(db: Session):
    '''
        args: 
            db: Database session
    '''
    try:
        return db.query(models.Place).order_by(models.Place.name).all()
    except Exception:
        logger.error(f"Error getting data",exc_info=True)


def insert(place: str, db: Session):
    '''
        args: 
            place: Name of place to store
            db: Database session
    '''
    address_details = GeoLocator.get_coordinates(place)
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


def delete(address_id: int, db: Session):
    '''
        args:
            address_id: Address id to delete
            db: Database session
    '''
    data = db.query(models.Place).filter(models.Place.id == address_id).first()

    if data is None:
        return {"message": f"No record found for address id {id}"}
    try:
        db.delete(data)
        db.commit()
        return {"message": f"Successfully deleted address id {id}"}
    except Exception:
        logger.error(f"Database issue", exc_info=True)
        db.rollback()
        return {"message": f"Database issue"}


def search_loc(place: str, db: Session) -> int:
    '''
        args:
            place: Name of place to check
            db: Database session
    '''
    data = db.query(models.Place).filter(models.Place.name.ilike(f"%{place}%")).first()
    if data is None:
        return None
    
    return data.id


def update(id: int, place: PlaceUpdate, db: Session, ):
    '''
        args:
            id: Record in database to be updated
            place: Schema for updating
            db: Database session
    '''
    updated = db.query(models.Place).filter(models.Place.id == id).first()
    try:
        setattr(updated, 'address',place.address)
        setattr(updated, 'latitude',place.latitude)
        setattr(updated, 'longitude',place.longitude)
        db.commit()
        logger.info(f'Record updated')

        return place
    except Exception:
        logger.error('Error updating record', exc_info=True)