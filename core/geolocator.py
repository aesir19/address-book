from geopy.geocoders import Nominatim
from logger_conf import logger

GEOLOCATOR = Nominatim(user_agent="Address Book")


def get_coordinates(location: str) -> dict:
    try:
        address_details = GEOLOCATOR.geocode(location)
        if address_details is None:
            logger.warn(f"No results found in {location}")
            return {"result": "Try searching again"}
        else:
            return address_details
    except Exception:
        logger.error("Geolocator issue", exc_info=True)


def get_address(latitude, longitude) -> dict:
    try:
        address_details = GEOLOCATOR.reverse(f"{latitude}, {longitude}")
        if address_details is None:
            logger.warn(f"No results found in {latitude}, {longitude}")
            return {"result": "Try searching again"}
        else:
            return address_details
    except Exception:
        logger.error("Geolocator issue", exc_info=True)
