from sqlalchemy import Column, Integer, String, Float, Text

from data_store.db_config import Base


class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)  # would use UUID for larger programs
    name = Column(String, nullable=False)
    address = Column(Text, nullable=False)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    
