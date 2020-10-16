# Light Sensor 

# Package import
import time
import board
import busio
import adafruit_tcs34725
import RPi.GPIO as GPIO 
import json

temp=  0
sample_rate= 4
class light_sensor:
    
    def __init__(self, datapin, pwr_pin  ):
        self.datapin = datapin
        self.pwr_pin = pwr_pin
        GPIO.setmode(GPIO.BCM) # use broadcom pin numbering
        GPIO.setup(self.pwr_pin, GPIO.OUT) # allocate power pin, set pin to output mode

        self.powerUp(pwr_pin)
        i2cbus = busio.I2C(board.SCL, board.SDA)
        
        self.sample_rate = 5
        #self.temp = light_sensor.color_temperature
        #self.lux = light_sensor.lux
        #self.time.sleep(0.5)  # allow for led to illuminate environment for accuracy
        # Initialize bus and constants.
        # Decision to power on sensor only when function is called in order to conserve energy
        
        self.light_sensor_config = adafruit_tcs34725.TCS34725(i2cbus)

    def powerUp(self, pwr_pin):
         # GPIO PIN  to power sensor
        
        GPIO.output(self.pwr_pin, 1) 

    def powerDown(self, pwr_pin):
         # GPIO PIN  to power sensor
        
        GPIO.output(self.pwr_pin, 0)

    # While loop to read and display sensor data
    def loopRead(self, pwr_pin):
        self.powerUp(pwr_pin)
  
        while True:
            self.powerUp(pwr_pin)
            time.sleep(0.5)
            temp =self.light_sensor_config.color_temperature
            lux = self.light_sensor_config.lux
            print("Temperature: {0}K Lux: {1}".format(temp, lux))
        # Sample rate for loop

            time.sleep(sample_rate)
            self.powerDown(pwr_pin)
            time.sleep(sample_rate)
        return temp + lux 

    # Function to read colour and luminosity
    def readColourLux(self, pwr_pin):
        self.powerUp(pwr_pin)
        temp = self.light_sensor_config.color_temperature
        lux = self.light_sensor_config.lux
        print("Temperature: {0}K Lux: {1}".format(temp, lux))
        return temp + lux 

    # Function to read luminosity
    def lux(self,pwr_pin):
        self.powerUp(pwr_pin)
        #lux = light_sensor.lux
        lux = self.light_sensor_config.lux
        print("Lux: {1}".format(temp, lux))
        return lux 

    # Function to read colour # Could be used for plant health? Green/Brown
    def colour(self):
        powerUp(self)
        colour = self.light_sensor_config.color_temperature
        print("Temperature: {0}K".format(temp))
        return lux 

    # Function to read individual colours
    def RGB(self):
        powerUp()
        print('Color: (Red {0}, Green {1}, Blue {2})'.format(*self.light_sensor_config.color_rgb_bytes))

    # Set Sample Rate
    def setSampleRate(self, Rate):
        sample_rate = Rate

    # Calibrate light sensor for daylight
    def sunlight(self):
        powerUp()
        sunset = self.light_sensor_config.lux

    # Calibrate light sensor for dark
    def sunset(self):
        powerUp()
        sunset = self.light_sensor_config.lux

    #colour()
    #lux()

    #readColourLux()
    #RGB()
    #GPIO.output(17, 0) # remove power from sensor

light_sensor_test = light_sensor(17, 17)
light_sensor_test.readColourLux(17)
light_sensor_test.loopRead(17)



