"""Main module."""

import json
from moisture_sensor import MoistureSensor
from gps import GPS
from light_sensor import light_sensor
import os
from datetime import datetime
from file_read_backwards import FileReadBackwards
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
        #loc = self.GPS.getLongLat()
        loc = self.GPS.getLongLat(self.GPS.getGLL())
        RMC_msg = self.GPS.getRMC()
        GGA_msg = self.GPS.getGGA()
        alt = GGA_msg.altitude
        dt = RMC_msg.datetime #time stamp
        str_datetime = dt.strftime("%Y-%m-%d %H:%M:%S")
        moisture = round(self.MS.singleRead()) #moisture level as a percentage
        try:
            light = self.LS.singleReadLux()
        except Exception as e:
            print(e)
            light = 100
            self.LS.powerDown(17)
        #lux = 0
        output = str_datetime + "\tMoisture: " + str(moisture) + "\tLux: " + str(light) + "\tLocation:" + loc + "\tAltitude: " + str(alt) +"\n"
        print(output)
        return Reading(moisture,light, RMC_msg)

        #return reading


    #def readingOK(self,reading):

    def loadProfile(self,name):
        with open("profiles.json", 'r') as f:
            try:
                profile = json.load(f)
                self.MAX_MOISTURE = profile[name]["moisture"][1]
                self.MIN_MOISTURE = profile[name]["moisture"][0]
                self.MAX_LUX = profile[name]["lux"][1]
                self.MIN_LUX = profile[name]["lux"][0]
                print("Profile " + '\'' + name + "\' loaded.\n")
            except Exception as e:
                print(e)
                print('Profile does not exist')

    def readingOK(self,reading, msg):
        ok = True
        if reading.moisture < self.MIN_MOISTURE or reading.moisture > self.MAX_MOISTURE or reading.lux < self.MIN_LUX or reading.lux > self.MAX_LUX:
            ok = False
            if reading.moisture < self.MIN_MOISTURE:
                msg[0] = "Moisture too low;"
            elif reading.moisture > self.MAX_MOISTURE:
                msg[0] = "Moisture too high;"
            if reading.lux < self.MIN_LUX:
                msg[0] = msg[0] + "lux too low\n"
            elif  reading.lux > self.MAX_LUX:
                msg[0] = msg[0] + "lux too high\n"
        else:
            msg[0] = 'Moisture and lux within range of current profile'
        return ok


    def logData(self, rmc, gga, gll, moist, lux):
        dt = rmc.datetime #time stamp
        time = dt.strftime("%Y-%m-%d %H:%M:%S")
        alt = gga.altitude
        loc = self.GPS.getLongLat(gll)
        string = time + "\t" + str(moist) + "\t" + str(lux) + "\t" + str(alt) + "\t\t" + loc + '\n'
        print(string)

        if os.path.exists('log.txt'):
            with open('log.txt', 'a') as f:
                f.write(string)
                f.close()
        else:
            with open('log.txt', 'a') as f:
                f.write("Time\t\t\tMoisture\t\tLux\t\t\tAltitude\t\tLocation\n")
                f.write(string)
                f.close()

    def last24Hrs(self, filename):
        try:
            now = datetime.utcnow()
            with FileReadBackwards('log.txt', encoding="utf-8") as f:
                for line in f:
                    try:
                        date = datetime.strptime(line[0:19], "%Y-%m-%d %H:%M:%S")
                    except:
                        break #if can't then we've reached the top line so break
                    if (now - date).days == 0: #within 24 hours
                        print(line)
                    else:
                        break
        except Exception as e:
            print(e)

#############################################################################
'''class for agro_kit reading:'''
#############################################################################

class Reading:

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


if __name__ == "__main__":
    myAG = AgroKit()
    myAG.loadProfile("test")
    lux = myAG.LS.singleReadLux()
    #myAG.logData(myAG.GPS.getRMC(), myAG.GPS.getGGA(), myAG.GPS.getGLL(), myAG.MS.singleRead(), lux)
    myAG.last24Hrs('log.txt')
