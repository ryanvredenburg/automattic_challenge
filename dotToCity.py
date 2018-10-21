#!/usr/bin/env python

import json
import requests
import googlemaps
import geopy.distance
from time import sleep

#Google Queries Per Scond Limit
gmaps_api_qps = 50
#set max query rate at half the limit
sleep_time = 1/(gmaps_api_qps/2)


gmaps = googlemaps.Client(key='KEY_HERE')

#coordinates of Automattic HQ
hq_coords = (37.744137, -122.42167)

response = requests.get("https://ac-map.automattic.com/?g=wpcom&cc=")
cities = json.loads(response.text)

for city in cities:

    city_coords = (city['lat'], city['lng'])

    #get distance between Automattic HQ and city
    city_distance = geopy.distance.vincenty(hq_coords, city_coords).km
    city.update({unicode('distance'):city_distance})
    #reverse locate the lat and long to find the city name
    reverse_geocode_result = gmaps.reverse_geocode((city['lat'], city['lng']))
    sleep(sleep_time)
    #find the city name within the API results
    city_name = "UNKNOWN"
    if len(reverse_geocode_result)>0:
        administrative = None
        locality = None
        for entry in reverse_geocode_result[0]['address_components']:
            if unicode('locality') in entry['types'] :
                locality = unicode(entry['long_name'])
            if unicode('administrative_area_level_1') in entry['types'] :
                administrative = unicode(entry['long_name'])
        #prefer locality over administrative_area_level_1
        if administrative is not None:
            city_name = administrative
        if locality is not None:
            city_name = locality
    else:
        #print "problem with this geocode"
        #print city
        pass
    city.update({unicode('name'):city_name})


print json.dumps(cities)
