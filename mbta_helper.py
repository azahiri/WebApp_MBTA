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
    return response_data
    pass
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
    response_data = get_json(url)
    result_lat_long = response_data['results'][0]['locations'][0]['latLng']
    # pprint(result_lat_long)
    latitude, longitude = result_lat_long['lat'], result_lat_long['lng']
    return latitude, longitude
    

print(get_lat_long("Prudential Center"))

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url_MBTA = f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance'
    response_data_MBTA =get_json(url_MBTA)
    pprint(response_data_MBTA)
    try:
        station = response_data_MBTA['data'][0]['attributes']['name']
        wheelchair = response_data_MBTA['data'][0]['attributes']['wheelchair_boarding']
        return station, wheelchair
    except: 
        return None, None
    pass
print(get_nearest_station("42.3489", "-71.08182"))

def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    lat, lng = get_lat_long(place_name)
    stop, station_accessible = get_nearest_station(lat, lng)
    return stop, station_accessible
    pass


# def main():
#     """
#     You can all the functions here
#     """
#     pass


# if __name__ == '__main__':
#     main()

# print(get_json(url))


