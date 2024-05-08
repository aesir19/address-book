from pydantic import BaseModel
from enum import Enum
from typing import Optional


class Place(BaseModel):
    id: int
    name: str
    address: str
    latitude: float
    longitude: float


class PlaceUpdate(BaseModel):
    address: str
    latitude: float
    longitude: float


class Coordinates(BaseModel):
    latitude: float
    longitude: float


# Scrapped due to time constraint and complexity of the used library
# class SpecificPlace(BaseModel):
#     id: int
#     name: str
#     street_name: str
#     barangay: str
#     city: str
#     district: str
#     region: str
#     postal_code: int
#     country: str
#     latitude: float
#     longitude: float





