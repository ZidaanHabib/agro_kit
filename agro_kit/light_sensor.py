# Light Sensor

# Package import
import time
import board
import busio
import adafruit_tcs34725
import RPi.GPIO as GPIO
import json

temp=  0
sample_rate= 0
class light_sensor:

    def __init__(self, datapin, pwr_pin  ):
        self.datapin = datapin
        self.pwr_pin = pwr_pin
        GPIO.setmode(GPIO.BCM) # use broadcom pin numbering
        GPIO.setup(self.pwr_pin, GPIO.OUT) # allocate power pin, set pin to output mode

        self.powerUp(pwr_pin)
        i2cbus = busio.I2C(board.SCL, board.SDA)

        self.sample_rate = 5

        self.light_sensor_config = adafruit_tcs34725.TCS34725(i2cbus)
        self.powerDown(pwr_pin)

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
            print("Colour Temperature: {0}K Lux: {1}".format(temp, lux))
        # Sample rate for loop

            time.sleep(sample_rate)
            self.powerDown(pwr_pin)
            time.sleep(sample_rate)



    def singleReadLux(self, pwr_pin):
        self.powerUp(pwr_pin)
        lux = self.light_sensor_config.lux
        self.powerDown(pwr_pin)
        #print(lux)
        return lux

    def singleReadColour(self, pwr_pin):
        self.powerUp(pwr_pin)
        colour = self.light_sensor_config.color_temperature
        self.powerDown(pwr_pin)
        #print(colour)
        return colour


    # Function to read luminosity
    def lux(self,pwr_pin):
        self.powerUp(pwr_pin)
        #lux = light_sensor.lux
        lux = self.light_sensor_config.lux
        print("Lux: {1}".format(temp, lux))
        return lux

    # Function to read colour
    def colour(self,pwr_pin):
        self.powerUp(pwr_pin)
        time.sleep(0.5)
        colour_temp = self.light_sensor_config.color_temperature
        print("Colour Temperature: {0}K".format(colour_temp))
        return colour_temp

    # Function to read individual colours
    def RGB(self,pwr_pin):
        self.powerUp(pwr_pin)
        print('Colour: (Red {0}, Green {1}, Blue {2})'.format(*self.light_sensor_config.color_rgb_bytes))

    # Set Sample Rate
    def setSampleRate(self, Rate):
        sample_rate = Rate

    # Calibrate light sensor for daylight
    def sunlight(self,pwr_pin):
        self.powerUp(pwr_pin)
        sunset = self.light_sensor_config.lux

    # Calibrate light sensor for dark
    def sunset(self,pwr_pin):
        self.powerUp(pwr_pin)
        sunset = self.light_sensor_config.lux

#  For testing

if __name__ == "__main__":
    light_sensor_test = light_sensor(17, 17)

    '''light_sensor_test.RGB(17)
    light_sensor_test.lux(17)
    light_sensor_test.powerUp(17)
    light_sensor_test.colour(17)
    light_sensor_test.singleReadColour(17)
    light_sensor_test.powerDown(17)'''

    print(light_sensor_test.singleReadLux(17))
