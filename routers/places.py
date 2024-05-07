from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from repository.place import *
from schemas import *
from data_store.db_config import get_db
from core.geolocator import *

router = APIRouter(tags=['Address Book'])


@router.get('/find-coordinates/{place}')
async def find_coordinates(request: Request, place: str):
    return get_coordinates(place)


@router.get('/find-address/{latitude}/{longitude}')
async def find_location(latitude: float, longitude: float):
    return get_address(latitude, longitude)
    # return get_address(coordinates)

# @router.get('/max-id')
# def test(request: Request, db: Session = Depends(get_db)):
#     return get_max_id(db)
#
# @router.post('insert-place')
# def insert_address(request: Request, db: Session = Depends(get_db)):
#     pass