from geopy.geocoders import Nominatim

GEOLOCATOR = Nominatim(user_agent="Address Book")


def get_coordinates(location: str) -> dict:
    address_details = GEOLOCATOR.geocode(location)
    data = {
        "address": address_details.address,
        "coordinates": (address_details.latitude, address_details.longitude)
    }
    return data


def get_address(latitude, longitude) -> dict:
    address_details = GEOLOCATOR.geocode(f"{latitude}, {longitude}")
    data = {
        "address": address_details.address,
        "coordinates": (address_details.latitude, address_details.longitude)
    }
    return data
