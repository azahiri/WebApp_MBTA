# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://open.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "1GJGgIOEKx3NdB0OyKuyc1DeZQNquhO2"
MBTA_API_KEY = "53fd682cdcda4fbdb2a462128846bb7f"


# A little bit of scaffolding if you want to use it
import urllib.request
import urllib.parse
import json
from pprint import pprint
url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)

    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint(response_data)
    return response_data

# pprint(get_json(url))

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    place_name = place_name.replace(' ', '%20')
    url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}'
    # print(url)  
    place_json = get_json(url)
    latitude = place_json['results'][0]['locations'][0]['latLng']['lat']
    longitude = place_json['results'][0]['locations'][0]['latLng']['lng']
    return latitude, longitude
    
# print(get_lat_long("86 Harrison Ave, Boston, MA 02111"))

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance'
    # print(url)
    station_json = get_json(url)
    # pprint(station_json)
    station_name = station_json['data'][0]['attributes']['name']
    # print(station_name)
    station_description = station_json['data'][0]['attributes']['description']
    if station_description:
        station_name = station_description
    # print(station_description)
    wheelchair_boarding = station_json['data'][0]['attributes']['wheelchair_boarding']
    if wheelchair_boarding == 0:
        wheelchair_accessible = 'Do not know if this station is wheelchair accessible or not.'
    elif wheelchair_boarding == 1:
        wheelchair_accessible = 'This station is wheelchair accessible.'
    else:
        wheelchair_accessible = 'This station is not wheelchair accessible.'
    return station_name, wheelchair_accessible

def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    return get_nearest_station(*get_lat_long(place_name))

# print(find_stop_near("86 Harrison Ave, Boston, MA 02111"))

def main():
    """
    You can all the functions here
    """
    place_name = "133 Mt Auburn St, Watertown, MA 02472" #This is the address of the best restaurant in Watertown
    print(get_lat_long(place_name))
    # print(get_nearest_station(*get_lat_long(place_name)))
    print(find_stop_near(place_name))

if __name__ == '__main__':
    main()

