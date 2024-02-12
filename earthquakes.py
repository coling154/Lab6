#!/usr/bin/python3
# earthquakes.py
import urllib.request
from ssl import _create_unverified_context
from json import loads

from urllib.request import urlopen
unverified_context = _create_unverified_context()

handle = urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson", context=unverified_context)

data = handle.read()        #read all JSON data
eData = loads(data)    #convert to Python
print(eData.keys())                #eData is a dictionary

import csv

data = eData['features']
with open('output.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['time', 'place', 'mag', 'magType', 'latitude', 'longitude', 'depth'])

    for feature in data:
        place = feature['properties']['place']
        if 'Syria' in place or 'Turkey' in place:
            time = feature['properties']['time']
            mag = feature['properties']['mag']
            magType = feature['properties']['magType']
            latitude = feature['geometry']['coordinates'][1]
            longitude = feature['geometry']['coordinates'][0]
            depth = feature['geometry']['coordinates'][2]
            csv_writer.writerow([time, place, mag, magType, latitude, longitude, depth])


