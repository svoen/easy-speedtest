#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

apikey = input("apikey for openrouteservice: ")
def geocode(text):

    url = "https://api.openrouteservice.org/geocode/search?&api_key={}&text={}".format(apikey, text)
    r = requests.get(url)
    response = r.json()
    json = response["features"][0]["geometry"]["coordinates"]
    lon = json[0]
    lat = json[1]
    return lat, lon
