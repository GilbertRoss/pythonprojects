#!/bin/python3
from datetime import datetime
import json
import turtle
import urllib.request

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

url2 = "http://api.open-notify.org/iss-now.json"
response2 = urllib.request.urlopen(url2)
result2 = json.loads(response2.read())

url3 = "http://api.open-notify.org/iss-pass.json?lat=46.496719&lon=11.358"
response3 = urllib.request.urlopen(url3)
result3 = json.loads(response3.read())

passengers = ["People in space " +  str(result['number'])]
people = result["people"]
iss_position = result2["iss_position"]
datet = result3["request"]
name = [(p["name"] +  " is in " + p["craft"])  for p in people]
position = [("ISS is at latitude " + iss_position["latitude"] + " and longitude " + iss_position["longitude"])]
date = [("On " + str(datetime.utcfromtimestamp(datet["datetime"]).strftime('%Y-%m-%d %H:%M:%S')) + " ISS is expected over BZ at latitude " + str(datet["latitude"]) +  " and longitude " + str(datet["longitude"]))]
separator = ["-------------"]
printable = [*passengers + name + separator + position + date]
print(*printable, sep = "\n")

with open('iss.txt', 'w') as f:
    for item in printable:
        f.write("%s\n" % item)
    
    
