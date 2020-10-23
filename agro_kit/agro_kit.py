"""Main module."""

import json
from moisture_sensor import MoistureSensor
from gps import GPS
#import light_sensor

class AgroKit:
    def __init__(self): #creating an agro_kit object consisting of a gps, moisture sensor object
        self.MS = MoistureSensor(21, 0, 7, 18)
        self.GPS = GPS()

    def read(self):
        dt = self.GPS.getRMC().datetime #time stamp
        str_datetime = dt.strftime("%Y-%m-%d %H:%M:%S")
        moisture = round(self.MS.singleRead()) #moisture level as a percentage
        #lum =
        output = str_datetime + " Moisture: " + str(moisture) + "%\n"
        print(output)



def createProfile(name, minMoisture, maxMoisture, minLux, maxLux):
    entry = { name: {"moisture": [minMoisture, maxMoisture], "lux": [minLux, maxLux]}}
    with open("profiles.json", "r") as f:
        try:
            profile = json.load(f)
        except:
            profile = {}
    with open("profiles.json", "w") as h:
        profile.update(entry)
        try:
            json.dump(profile,h, indent=4)
        except Exception as e:
            print(e)

s
myAG = AgroKit()
myAG.read()
#createProfile("test", 0,100, 100, 200)
