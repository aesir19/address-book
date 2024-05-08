from fastapi import APIRouter, Depends, Request, Body
from sqlalchemy.orm import Session

from repository.place import *
from schemas import *
from data_store.db_config import get_db
from logger_conf import logger
from core.geolocator import *

router = APIRouter(tags=['Address Book'])


@router.get('/get-all-address')
async def get_records(db: Session = Depends(get_db)):
    return get_all(db)


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
        exisiting_id = search_loc(place, db)
        if exisiting_id is None:
            return insert(place, db)
        else:
            return {'message': 'Place is already existing'}
    except Exception:
        logger.error(f"Error inserting data", exc_info=True)


@router.delete('/delete-address/{id}')
async def delete_address(id: int, db: Session = Depends(get_db)):
    try:
        logger.info(f"Deleting address id {id}")
        return delete(id, db)
    except Exception:
        logger.error("Error deleting", exc_info=True)


@router.put('/update-address/{place}')
async def update_address(place: str, request: PlaceUpdate, db: Session = Depends(get_db)):
    try:
        logger.info(f'Updating record for {place}...')
        print(request)
        id = search_loc(place, db)
        if id is not None:

            return update(id, db, request)
        else:
            return {'message': f'No location found, please try again'}
    except Exception:
        logger.error("Error searching for record", exc_info=True)
