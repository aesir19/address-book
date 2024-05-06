from sqlalchemy import Column, Integer, String, Float

from .db_config import Base

class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True) # would use UUID for larger programs
    name = Column(String, nullable=False)
    street_number = Column(Integer, nullable=False)
    street_name = Column(String, nullable=False)
    barangay_name = Column(String, nullable=False)
    city_name = Column(String, nullable=False)
    postal_code = Column(Integer, nullable=True)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    
