from pydantic import BaseModel
from enum import Enum
from typing import Optional


class Place(BaseModel):
      id: int
      name: str
      house_number: int
      street_name: str
      barangay: str
      city: str
      postal_code: Optional[str]
      latitue: float
      longitude: float

