"""Main module."""

import json
from moisture_sensor import MoistureSensor
from gps import GPS
from light_sensor import light_sensor

###########################################################################3#
'''AgroKit class to interface with hardware'''
###############################################################################
class AgroKit:


    def __init__(self): #creating an agro_kit object consisting of a gps, moisture sensor object
        #creating individual sensor instances
        self.MS = MoistureSensor(21, 0, 7, 18)
        self.GPS = GPS()
        self.LS = light_sensor(17, 17)
        #defaults:
        MAX_MOISTURE = 100
        MIN_MOISTURE = 0
        MAX_LUX = 500
        MIN_LUX = 0


    def read(self):
        gps_msg = self.GPS.getRMC()
        dt = gps_msg.datetime #time stamp
        str_datetime = dt.strftime("%Y-%m-%d %H:%M:%S")
        moisture = round(self.MS.singleRead()) #moisture level as a percentage
        #lum =
        output = str_datetime + " Moisture: " + str(moisture) + "%\n"
        reading = Reading(moisture,0, gps_msg)
        print(output)
        return reading


    def readingOK(self,reading):


    def loadProfile(self,name):
        with open("profiles.json", 'r') as f:
            try:
                profile = json.load(f)
                self.MAX_MOISTURE = profile[name]["moisture"][1]
                self.MIN_MOISTURE = profile[name]["moisture"][0]
                self.MAX_LUX = profile[name]["lux"][1]
                self.MIN_LUX = profile[name]["lux"][0]
            except Exception as e:
                print(e)

#############################################################################

#class for agro_kit reading:
class Reading(self):

    def __init__(self, moisture, lux, gps):
        self.moisture = moisture
        self.lux = lux
        self.gps = gps
#############################################################################

###############################################################################
''' General Library methods'''
#######################################################################33#
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

####################################################################################


myAG = AgroKit()
myAG.loadProfile("test")
myAG.read()
