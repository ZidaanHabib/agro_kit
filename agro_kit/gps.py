import json
import serial
from time import sleep
import pynmea2 as nmea

class GPS:

    #Static Var
    ser = serial.Serial ("/dev/ttyS0", 9600 , timeout=1)


    def __init__(self, baud_rate = 9600, timeout = 5):
        self.baud_rate = baud_rate
        self.timeout = timeout
        #ser = serial.Serial ("/dev/ttyS0", self.baud_rate, self.timeout)
        self.ser.baudrate = baud_rate
        self.ser.timeout = timeout


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





#used for testing
if __name__ == "__main__":
    myGPS = GPS()
    x = myGPS.getRMC()
    print(x.latitude + "\n")
    y = myGPS.getGLL()
    print(x.latitude + "\n")
