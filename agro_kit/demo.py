
import gps
import moisture_sensor
import light_sensor

myGPS = GPS()
with open("../.gmaps_key", "r") as f:
    API_KEY = f.readline().strip()
    f.close()
GPS.setAPIKey(API_KEY)
