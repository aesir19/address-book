# address-book
Pasig Address Book


## How to setup
-- Prerequisite: atleast python version 3.8
1. Clone the repository using this link https://github.com/aesir19/address-book.git
2. Create a python environment using the command `python -m venv 'your-env-name'`
3. Activate your virtual environment by navigating through your virtual environment folder > Scripts > then type `activate` if you are in Windows.
- In linux environments, type in the command `source 'your-env-name'/bin/activate`
4. Install the packages by running the command `pip install -r requirements.txt`
5. Once done, run the command `python3 main.py` to run the program and head over to "localhost:8000/docs" to view the APIs

## How to use APIs

**/get-all-address**
- No input needed, returns all data from the database

**/find-coordinates/place**
- Accepts name of a place as input, returns address and coordinates of the given place

**/find-address/latitude/longitude**
- Accepts inputs for latitude and longitude as coordinates, returns address and coordinates

**/search-and-input/place**
- Accepts name of a place as input and store the record in the database

**/delete-place/id**
- Accepts id of a place and deletes the record in the database

**update-address/place**
- Accepts name of the place as well as address and coordinates and updates the record