from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from repository.place import *
from data_store.db_config import get_db

router = APIRouter(tags=['Address Book'])

@router.get('/max-id')
def test(request: Request, db: Session = Depends(get_db)):
    return get_max_id()

@router.post('insert-place')
def insert_address(request: Request, db: Session = Depends(get_db)):
    pass