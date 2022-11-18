# Name: Alisha Gursahaney
# Net Id: amg9zd

import math
import webbrowser

# DO NOT MODIFY the following function; use as is
def distance_between(lat_1, lon_1, lat_2, lon_2):
    """Uses the "great circle distance" formula and the circumference of the earth
    to convert two GPS coordinates to the miles separating them"""
    lat_1, lon_1 = math.radians(lat_1), math.radians(lon_1)
    lat_2, lon_2 = math.radians(lat_2), math.radians(lon_2)
    theta = lon_1 - lon_2
    dist = math.sin(lat_1)*math.sin(lat_2) + math.cos(lat_1)*math.cos(lat_2)*math.cos(theta)
    dist = math.acos(dist)
    dist = math.degrees(dist)
    dist = dist * 69.06         # 69.09 = circumference of earth in miles / 360 degrees
    return dist


file = open("chickfila.csv")
smallestdistance = 10000000

lat = float(input('Enter a Latitude: '))
long =float(input('Enter a Longitude: '))
for line in file:
    readlines = line.split(',')
    saveLat = float(readlines[0])
    saveLong = float(readlines[1])
    distance = distance_between(lat, long, saveLat, saveLong)
    if distance<smallestdistance:
        smallestdistance = distance
        smallestInfoLine = readlines
address = smallestInfoLine[4]+smallestInfoLine[5]+''+smallestInfoLine[6]
address = address.replace(' ', '+')
webAddress='http://maps.google.com/maps?q=' + address
webbrowser.open(webAddress)
