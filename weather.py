from datetime import datetime
import json
import turtle
import urllib.request
import requests

city = input("Enter city name and country (Manchester, UK): ")


url = "https://us1.locationiq.com/v1/search.php?key=a4e6722b636ab1&q=" + city + "&format=json"


response = urllib.request.urlopen(url)
result = json.loads(response.read())


firstResult = result[0]
lat = firstResult['lat']
lon = firstResult['lon']

url2 = "https://weather.cit.api.here.com/weather/1.0/report.json?product=observation&latitude=" + lat + "&longitude=" + lon + "&oneobservation=true&app_id=DemoAppId01082013GAL&app_code=AJKnXv84fjrb0KIHawS0Tg"

response2 = urllib.request.urlopen(url2)
result2 = json.loads(response2.read())

observations = result2["observations"]



location = observations["location"]
zero = location[0]
observation = zero["observation"]
ob0 = observation[0]
description = ob0["skyDescription"]
temperature = ob0["temperature"]

print("Today in " + city + " the weather is " + description + ". Today's temperature will be " + temperature + " celsius")
