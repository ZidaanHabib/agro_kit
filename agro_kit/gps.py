import json
import serial
from time import sleep
from time import time
import pynmea2 as nmea
import requests
import sys

class GPS():

    BAUD_RATES = [4800, 9600, 14400, 19200, 38400, 57600, 115200]
    BAUD_RATE_CHKSUMS = {'4800': "48", '9600': '4B', '14400': '75', '19200': '7E', '38400': '7B', '57600': '70', '115200': '43'}



    #Static Var
    #ser = serial.Serial ("/dev/ttyS0", 9600 , timeout=1)
    API_KEY = '' # empty by default


    def __init__(self, baud_rate = 9600, timeout = 5):
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.ser = serial.Serial ("/dev/ttyS0", self.baud_rate, self.timeout)
        self.ser.baudrate = baud_rate
        self.ser.timeout = timeout


#######################################################################################3ss
#Configuration methods
#######################################################################################3

#set baud rate of GPS receiver:

#note that only baud rates of 4800, 9600, 14400, 19200, 38400, 57600, 115200 are allowed
    def setGPSBaudRate(self, baud_rate): #NOTE: STILL IN DEVELOPMENT - DO NOT USE
        if baud_rate in GPS.BAUD_RATES:
            str_baud_rate = str(baud_rate)
            cmd = '$PQBAUD,W,' + str_baud_rate + '*' + GPS.BAUD_RATE_CHKSUMS[str_baud_rate] + "\r\n"
            self.ser.write(cmd.encode())
            sleep(0.1)
            self.ser.baudate = baud_rate # set /dev/ttyS0 baudrate as well
            sleep(1.2)
            response = self.ser.readline().decode()
            print(response)
        else:
            print("Error - invalid baud rate. Can only choose from 4800, 9600, 14400, 19200, 38400, 57600, 115200.")

    def enableURC(self, mode, save): #NOTE: STILL IN DEVELOPMENT - DO NOT USE
        arg1, arg2, = '0','0'
        if mode:
            arg1 = 1
        if save:
            arg2 = 1
        cmd = "$PQEPE,W," + str(mode) + ',' + str(save)
        chksm = ord(cmd[1])
        for i in range(2,len(cmd)):
            chksm ^= ord(cmd[i])
        self.ser.write("$PQEPE,W,0,0*2A\r\n".encode())
        #response = self.ser.readline().decode()
        #print(response)

    def coldstart(self):
        self.ser.write("$PMTK103*30\r\n".encode())

    def fullColdStart(self):
        self.ser.write("$PMTK104*37\r\n".encode())

    def warmStart(self):
        self.ser.write("$PMTK102*31\r\n".encode())

    def hotStart(self):
        self.ser.write("$PMTK101*32\r\n".encode())
#########################################################################
#Methods to get different NMEA message types from GPS module:

    #recommended minimum position data
    def getRMC(self):
        nmea_msg = ''
        while nmea_msg[0:6] != '$GPRMC':
            nmea_msg = self.ser.readline().decode()
            nmea_msg = nmea_msg[0:len(nmea_msg)-2] #exclude <CR><LF> when parsing
        nmea_obj = nmea.parse(nmea_msg)
        return nmea_obj

    def getVTG(self):
        nmea_msg = ''
        while nmea_msg[0:6] != '$GPVTG':
            nmea_msg = self.ser.readline().decode()
            nmea_msg = nmea_msg[0:len(nmea_msg)-2] #exclude <CR><LF> when parsing
        nmea_obj = nmea.parse(nmea_msg)
        return nmea_obj

    def getGGA(self):
        nmea_msg = ''
        while nmea_msg[0:6] != '$GPGGA':
            nmea_msg = self.ser.readline().decode()
            nmea_msg = nmea_msg[0:len(nmea_msg)-2] #exclude <CR><LF> when parsing
        nmea_obj = nmea.parse(nmea_msg)
        return nmea_obj

    def getGSA(self):
        nmea_msg = ''
        while nmea_msg[0:6] != '$GPGSA':
            nmea_msg = self.ser.readline().decode()
            nmea_msg = nmea_msg[0:len(nmea_msg)-2] #exclude <CR><LF> when parsing
        nmea_obj = nmea.parse(nmea_msg)
        return nmea_obj

    def getGSV(self):
        nmea_msg = ''
        while nmea_msg[0:6] != '$GPGSV':
            nmea_msg = self.ser.readline().decode()
            nmea_msg = nmea_msg[0:len(nmea_msg)-2] #exclude <CR><LF> when parsing
        nmea_obj = nmea.parse(nmea_msg)
        return nmea_obj

    def getGLL(self):
        nmea_msg = ''
        while nmea_msg[0:6] != '$GPGLL':
            nmea_msg = self.ser.readline().decode()
            nmea_msg = nmea_msg[0:len(nmea_msg)-2]  #exclude <CR><LF> when parsing
        nmea_obj = nmea.parse(nmea_msg)
        return nmea_obj

    def continuousRead(self): #continously print raw data to terminal
        while True:
            try:
                print(self.ser.read())
                sleep(0.1)
            except KeyboardInterrupt:
                break

    def getPQEPE(self):
        nmea_msg = ''
        while nmea_msg[0:6] != '$PQEPE':
            nmea_msg = self.ser.readline().decode()
            nmea_msg = nmea_msg[0:len(nmea_msg)-2]  #exclude <CR><LF> when parsing
        #nmea_obj = nmea.parse(nmea_msg)
        print(nmea_msg)

    def getNumSats(self):
        nmea_obj = self.getGGA()
        num_sats = nmea_msg.num_sats
        print(num_sats)
        return num_sats

    def getLongLat(self, gll):
        #nmea_obj = self.getGLL()
        nmea_obj = gll
        res = str(nmea_obj.latitude) + ',' + nmea_obj.lat_dir + ','+ str(nmea_obj.longitude) + "," + nmea_obj.lon_dir
        return res

    def getAltitude(self):
        nmea_obj = self.getGGA()
        alt = nmea_obj.altitude
        return alt


#######################################################################################3
#Methods for the Distance Matrix API:
#######################################################################################3


    def distanceTo(self, dst_lat, dst_long):
        data = self.getGLL()
        origin_lat = data.latitude
        origin_long = data.longitude
        return GPS.distanceFromTo(origin_lat, origin_long, dst_lat, dst_long)

    #set Google API key:
    @classmethod
    def setAPIKey(cls, key):
        GPS.API_KEY = key


    #Calculate distance from specified coords to destination coords in meters:
    @classmethod
    def distanceFromTo(cls, origin_lat, origin_long, dst_lat, dst_long):
        #if origin_lat.isNumeric() and origin_lat.isNumeric() and isNumeric(dst_lat) and isNumeric(dst_long):
        url1 = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
        url2 = 'origins='+str(origin_lat) + ',' + str(origin_long)
        url3 = '&destinations=' +str(dst_lat) + ',' + str(dst_long)
        url4 = "&mode=car&key=" + GPS.API_KEY
        url = url1 + url2 + url3 + url4
        output = requests.get(url).json() #sending get request to google maps Distance MatriX API
        return output["rows"][0]["elements"][0]["distance"]["value"]



#used for testing
if __name__ == "__main__":
    myGPS = GPS()
    with open("../.gmaps_key", "r") as f:
        API_KEY = f.readline().strip()
        f.close()
    GPS.setAPIKey(API_KEY)
    dst_lat, dst_long = -26.146446, 28.041632
    #print(myGPS.getRMC())
    #myGPS.ser.write(b"$PMTK101*32\r\n")
    #print(myGPS.getLongLat())
    print(myGPS.getGLL())
