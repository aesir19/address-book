from fastapi import APIRouter, Depends, Request, Body
from sqlalchemy.orm import Session

from repository.place import *
from schemas import *
from data_store.db_config import get_db
from logger_conf import logger
from core.geolocator import *

router = APIRouter(tags=['Address Book'])


@router.get('/find-coordinates/{place}')
async def find_coordinates(place: str):
    try:
        logger.info(f"Getting coordinates for {place}")
        address_details = get_coordinates(place)
        return {
            "address": address_details.address,
            "coordinates": (address_details.latitude, address_details.longitude)
        }
    except Exception:
        logger.error(f"Error getting coordinates", exc_info=True)


@router.get('/find-address/{latitude}/{longitude}')
async def find_location(latitude: float, longitude: float):
    try:
        logger.info(f"Getting address for coordinates ({latitude}, {longitude})")
        address_details = get_address(latitude,longitude)
        return {
            "address": address_details.address,
            "coordinates": (address_details.latitude, address_details.longitude)
        }
    except Exception:
        logger.error(f"Error getting address", exc_info=True)



@router.post('/search-and-insert/{place}')
async def insert_address(place: str, db: Session = Depends(get_db)):
    try:
        logger.info(f"Getting and storing coordinates for {place}")
        address_details = get_coordinates(place)
        details = [place, address_details.address, address_details.latitude,
                   address_details.longitude]
        print(details)
        return insert(place, db)
    except Exception:
        logger.error(f"Error inserting data", exc_info=True)


@router.delete('/delete-place/{id}')
async def delete_address(id: int, db: Session = Depends(get_db)):
    try:
        logger.info(f"Deleting address id {id}")
        delete(id, db)
    except Exception:
        logger.error("Error deleting", exc_info=True)