
import gps
from simplepush import send, send_encrypted
import moisture_sensor
from time import sleep
#import light_sensor

myGPS = gps.GPS(9600) # create an instance of the GPS class


#demo reading raw gps data:
#myGPS.continuousRead()
#sleep(1)

#print(myGPS.getGLL())
#sleep(1)
#print(myGPS.getGSV())

#We can also calculate the distance to a set of long and lat coordinates
with open("../.gmaps_key", "r") as f:
    API_KEY = f.readline().strip()
    f.close()
#gps.GPS.setAPIKey(API_KEY) # sets our API key that will be used for some of the google maps functions
#dst_lat, dst_log = -34.029023, 18.444479 # location of the Constantia Emporium
#dst_lat, dst_log = -26.145984, 28.041307 # directions to Rosebank mall JHB

#print("Distance is " + str(myGPS.distanceTo(-34.029023, 18.444479)) + "m to the Constantia Emporium")
#msg = myGPS.ser.readline()
#print(msg.decode())

#print(myGPS.getGLL())



#################################
#Moisture sensor:
#########################

myMS = moisture_sensor.MoistureSensor(21, 0, 7, 18)

#myMS.calibrate_max() # make sure moisture sensor is submerged
#sleep(0.1)
#myMS.calibrate_min() # submerege moisture sensor is dry

#open up the config.json file to confirm

reading = myMS.singleRead()
print(reading)
#send("9GC4Df", "Peer Review Demo", "Moisture reading value: " + str(reading), "event")
# create peer review test range:

myMS.createRange(30, 50, "peer review test")

# send a push notification to our device:
