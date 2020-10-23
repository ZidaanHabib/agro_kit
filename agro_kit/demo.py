
import gps
import moisture_sensor
from time import sleep
#import light_sensor

myGPS = gps.GPS() # create an instance of the GPS class


#demo reading raw gps data:
myGPS.continuousRead()
sleep(1)

print(myGPS.getGLL())
sleep(1)
print(myGPS.getGSV())

#We can also calculate the distance to a set of long and lat coordinates
with open("../.gmaps_key", "r") as f:
    API_KEY = f.readline().strip()
    f.close()
gps.GPS.setAPIKey(API_KEY) # sets our API key that will be used for some of the google maps functions
dst_lat, dst_log = -34.029023, 18.444479 # location of the Constantia Emporium
print("Distance is " + myGPS.distanceTo(-34.029023, 18.444479) + "m to the Constantia Emporium")
