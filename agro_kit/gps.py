import json
import serial
from time import sleep
import pynmea2 as nmea

class GPS:

    #Static Var
    ser = serial.Serial ("/dev/ttyS0", 9600 , 1)


    def __init__(self, baud_rate, timeout = 5):
        self.baud_rate = baud_rate
        self.timeout = timeout
        #ser = serial.Serial ("/dev/ttyS0", self.baud_rate, self.timeout)
        ser.setBaudrate(baud_rate)
        ser.setTimeout(timeout)


    #recommended minimum position data
    def getRMC(self):
        nmea_msg = ''
        while nmea_msg != '$GPRMC':
            nmea_msg = ser.readline().decode()
    def getVTG(self):
        nmea_msg = ''
        while nmea_msg != '$GPVTG':
            nmea_msg = ser.readline().decode()
    def getGGA(self):
        nmea_msg = ''
        while nmea_msg != '$GPGGA':
            nmea_msg = ser.readline().decode()
    def getGSA(self):
        nmea_msg = ''
        while nmea_msg != '$GPGSA':
            nmea_msg = ser.readline().decode()
    def getGSV(self):
        nmea_msg = ''
        while nmea_msg != '$GPGSV':
            nmea_msg = ser.readline().decode()
    def getGLL(self):
        nmea_msg = ''
        while nmea_msg != '$GPGLL':
            nmea_msg = ser.readline().decode()



#used for testing
if __name__ == "__main__":
    ser = serial.Serial ("/dev/ttyS0", 9600, 5)
    nmea_msg = ''
    for i in range(10):
        nmea_msg += ser.readline().decode()
    print(nmea_msg)
