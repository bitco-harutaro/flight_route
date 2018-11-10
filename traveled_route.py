# -*- coding: utf-8 -*-


import csv
import codecs
import geocoder


#csvファイルから旅行先を読み取ってリストplacesに順に追加していく
places = []

with open("sample.csv", "r") as f:
    placesdata = csv.reader(f)
    places = [x for x in placesdata]

for x in places:
    print(x)


#placesにある地名の座標をgeocoderで取得し、リストcoordinatesに順に追加していく
coordinates = []

for x in places:
    a = geocoder.osm(str(x))
    b = a.latlng
    coordinates.append(b)

for x in coordinates:
    print(x)
