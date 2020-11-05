import time
import board
import busio
import adafruit_tcs34725
import RPi.GPIO as GPIO

# default values:
temp=  0
sample_rate= 0
pwr_pin = 17

class light_sensor:

    def __init__(self, datapin, pwr_pin  ):
        """Instantiate Light Sensor object using keyword arguments."""
        self.datapin = datapin
        self.pwr_pin = pwr_pin
        GPIO.setmode(GPIO.BCM) # use broadcom pin numbering on Raspberry Pi
        GPIO.setup(self.pwr_pin, GPIO.OUT) # Allocate power pin, set pin to output mode
        self.powerUp(pwr_pin)
        i2cbus = busio.I2C(board.SCL, board.SDA) # Setup i2c bus
        self.sample_rate = 5
        self.light_sensor_config = adafruit_tcs34725.TCS34725(i2cbus)

#######################################################################################
#Configuration methods
#######################################################################################

    def set_pwr_pin(self,pin_num):
        """ Set power source pin number to light sensor object.
        
        arguments:
        pin_num -- power supply pin to light sensor
        """
        self.pwr_pin = pin_num


    def setSampleRate(self, Rate):
        """Input rate to set the refresh display rate of continous read functions.
        
        arguments:
        Rate -- delay rate in seconds
        """
        sample_rate = Rate

    def sunlight(self,pwr_pin):
        """Input pwr_pin. Calibrate light sensor for full sunshine lux value, light sensor reads lux value and returns sunlight lux value.
        
        arguments:
        pwr_pin -- allocated pwr_pin to light sensor
        """
        self.powerUp(pwr_pin)
        sunlight = self.light_sensor_config.lux
        return sunlight

    def sunset(self,pwr_pin):
        """Calibrate light sensor for sunset lux value, light sensor reads lux value and returns sunset lux value.
         
        arguments:
        pwr_pin -- allocated pwr_pin to light sensor
        """
        self.powerUp(pwr_pin)
        sunset = self.light_sensor_config.lux
        return sunset

    def powerUp(self, pwr_pin):
        """Turn on power source (GPIO output) to light sensor.
        
        arguments:
        pwr_pin -- allocated pwr_pin to light sensor
        """
        GPIO.output(self.pwr_pin, 1)

    def powerDown(self, pwr_pin):
        """Turn off power source (GPIO output) to light sensor.
        
        arguments:
        pwr_pin -- allocated pwr_pin to light sensor
        """
        GPIO.output(self.pwr_pin, 0)

#######################################################################################
#Sensor interrogation methods
#######################################################################################

    def loopRead(self, pwr_pin):
        """Continuously read light sensor lux and colour temp, print, loop.

        arguments:
        pwr_pin -- allocated pwr_pin to light sensor
        """

        self.powerUp(pwr_pin)
        while True:
            self.powerUp(pwr_pin)
            time.sleep(0.5)
            temp =self.light_sensor_config.color_temperature
            lux = self.light_sensor_config.lux
            print("Colour Temperature: {0}K Lux: {1}".format(temp, lux))
            time.sleep(sample_rate)

    def singleReadLux(self):
        """Read light sensor lux value of object once and return lux."""
        lux = self.light_sensor_config.lux
        return lux

    def singleReadColour(self):
        """Read light sensor colour value of object once and return colour."""
        self.powerUp(pwr_pin)
        colour = self.light_sensor_config.color_temperature
        self.powerDown(pwr_pin)
        return colour

    def lux(self,pwr_pin):
        """Read light sensor lux value, format and print, return lux.
        
        arguments:
        pwr_pin -- allocated pwr_pin to light sensor
        """
        self.powerUp(pwr_pin)
        lux = self.light_sensor_config.lux
        print("Lux: {1}".format(temp, lux))
        return lux

    def colour(self,pwr_pin):
        """Read light sensor colour value, format and print, return colour.
        
        arguments:
        pwr_pin -- allocated pwr_pin to light sensor
        """
        self.powerUp(pwr_pin)
        time.sleep(0.5)
        colour_temp = self.light_sensor_config.color_temperature
        print("Colour Temperature: {0}K".format(colour_temp))
        return colour_temp

    def RGB(self,pwr_pin):
        """Read light sensor RGB values, format and print.
        
        arguments:
        pwr_pin -- allocated pwr_pin to light sensor
        """
        self.powerUp(pwr_pin)
        print('Colour: (Red {0}, Green {1}, Blue {2})'.format(*self.light_sensor_config.color_rgb_bytes))







