from geopy.geocoders import Nominatim
from logger_conf import logger

GEOCODER = Nominatim(user_agent="Address Book")

class GeoLocator:
    '''
        Class object for the addresses
    '''

    def __init__(self):
        pass


    @staticmethod
    def get_coordinates( location: str) -> dict:
        '''
            Get address details and coordinates by location name
            
            args:
                location: Name of location to search
        '''
        try:
            address_details = GEOCODER.geocode(location)
            if address_details is None:
                logger.warn(f"No results found in {location}")
                return {"result": "Try searching again"}
            else:
                return address_details
        except Exception:
            logger.error("Geolocator issue", exc_info=True)


    @staticmethod
    def get_address(latitude: float, longitude: float) -> dict:
        '''
            Get address details and coordinates by coordinates
            
            args:
                latitude: latitude of location to search
                longitude: longitude of location to search
        '''
        try:
            address_details = GEOCODER.reverse(f"{latitude}, {longitude}")
            if address_details is None:
                logger.warn(f"No results found in {latitude}, {longitude}")
                return {"result": "Try searching again"}
            else:
                return address_details
        except Exception:
            logger.error("Geolocator issue", exc_info=True)
