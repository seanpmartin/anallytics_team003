#!/usr/bin/env python

import sys

sys.path.append("/home/tug37917/census/census-0.8.1/census")
sys.path.append("/home/tug37917/census/us-0.9.1/us")

import core
from core import Census
import states


import geopy
import geopy.geocoders
from geopy.geocoders import Nominatim
geolocator = Nominatim()

#import pandas as pd

import plotly as py
from plotly.graph_objs import *

import glob
from lxml import etree

PLOTLY_USERNAME = "AlexGetka"
PLOTLY_API_KEY = "LFOm8OMlc3a0Iy4h0kwU"
py.tools.set_credentials_file(username=PLOTLY_USERNAME, api_key=PLOTLY_API_KEY)

# US Census API key
CENSUS_API_KEY = "e9e86beddcadb597e61440c5c498254452434332"

# Census varible IDs for populations of interest
ID_FINNISH = "B04004_039E"
ID_ISRAELI = "B04004_050E"
ID_IRISH = "B04004_049E"
ID_SCANDINAVIAN = "B04004_065E"

# Initialize census session
c = Census(CENSUS_API_KEY)

places = c.acs5.get(('NAME', ID_FINNISH, ID_ISRAELI, ID_IRISH, ID_SCANDINAVIAN),
          {'for': 'place:*', 'in': 'state:*'})

for item in places:
        item['NAME'] = item['NAME'].replace("CDP", '').replace("city", '') \
        .replace("urban county", '').replace("village", '') \
        .replace(" borough", '').replace(" ,", ',')

def sortPlaces(places):
        # Sort by total members populations of interest.
        # One could assign weights to each population
        # if we knew relative incidences.
        places = sorted(places, key=lambda k: k[ID_FINNISH] + k[ID_ISRAELI] \
        + k[ID_IRISH] + k[ID_SCANDINAVIAN])

#print places

trials = glob.glob('./clinics/*.xml')
facilities = []

for trial in trials:
        data = etree.parse(trial)
        indexes = []
        if data.xpath("//facility/name/text()") != None:
                for index, item in enumerate(data.xpath("//facility/address/country/text()")):
                        if item == "United States":
                                indexes.append(index)
                for index in indexes:
                        city = data.xpath("//facility/address/city/text()")[index]
                        state = data.xpath("//facility/address/state/text()")[index]
                        site =  city + ", " + state
                        facilities.append(site)

placesWithFacilities = set(facilities)

intersectPlaces = []
lat_list = []
lon_list = []
pop_list = []

sortPlaces(places)

for i in range(len(places)):
        if places[i]['NAME'] in placesWithFacilities:
                intersectPlaces.append(places[i]['NAME'])
                pop_list.append(int(places[i][ID_FINNISH]) + int(places[i][ID_ISRAELI]) + int(places[i][ID_IRISH]) + int(places[i][ID_SCANDINAVIAN]))
                print "DEBUG: found a place: ", places[i]['NAME']

#sortPlaces(intersectPlaces)

for place in intersectPlaces:
        geo_site = geolocator.geocode(place)
        lat_list.append(geo_site.latitude)
        lon_list.append(geo_site.longitude)

scl = [ [0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
    [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"] ]

data = [ dict(
        type = 'scattergeo',
        locationmode = 'USA-states',
        lon = lon_list,
        lat = lat_list,
        text = intersectPlaces,
        mode = 'markers',
        marker = dict(
            size = 5,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'square',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorscale = scl,
            cmin = 0,
            color = pop_list,
            cmax = max(pop_list),
            colorbar=dict(
                title="Members of Populations of Interest"
            )
        ))]

layout = dict(
        title = 'Cities most capable of holding successful clinical trials<br>(Hover for city names)',
        colorbar = True,
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ),
    )

# print intersectPlaces, pop_list
fig = dict( data=data, layout=layout )
py.plotly.plot( fig, validate=False, filename='LSDclinicaltrials' )

#keys_places = set(facilities).intersection(set


#testlocation = geolocator.geocode(places[1]["NAME"].replace("CDP", ''))
#print places
#print testlocation.address
#print (testlocation.latitude, testlocation.longitude)
