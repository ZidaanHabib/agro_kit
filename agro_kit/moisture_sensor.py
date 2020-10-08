#import grovepi
from time import sleep
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import RPi.GPIO as GPIO

class MoistureSensor:

#default and constant values:
    #datapin = 21 # MISO pin of pi zero
    #adcChannel = 7 # pin number of MCP3008  that is reading analog input
    #dly = 0.1 #0.1 second delay betweenr eadings by default
    SPI_TYPE = 'HW'
    #SPI_PORT = 0 # using CE0 port on pi
    #SPI_DEV = 0
    #MAX_READING= 1
    #MIN_READING = 0
    #pwr_pin = 18 # gpio pin used to power moisture sensor

    def __init__(self, datapin, SPI_PORT, adcChannel, pwr_pin  ):
        self.datapin = datapin
        self.SPI_PORT = SPI_PORT
        self.SPI_DEV = SPI_PORT
        self.adcChannel = adcChannel
        self.pwr_pin = pwr_pin
        self.dly = 0.1
        self.MAX_READING = 1
        self.MIN_READING = 0
        GPIO.setmode(GPIO.BCM) # use broadcom pin numbering
        GPIO.setup(self.pwr_pin, GPIO.OUT) # set pin to output mode


        self.mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(self.SPI_PORT, self.SPI_DEV))

    def set_pwr_pin(self,pin_num):
        self.pwr_pin = pin_num

    def setDelay(self, delay):
        self.dly = delay
    def setPin(self, pin):
        self.datapin = pin #set data pin to be something else if another microcontroller is used with a serial connection

    def init_SPI(self):
        #Adafruit_GPIO allows software or hardware SPI. We are using hardware
        self.SPI_TYPE = 'HW'
        self.SPI_PORT = 0 # using CE0 port on pi
        self.SPI_DEV = 0

        mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEV))


    #user must submerge sensor in water
    def calibate_max(self):
        self.MAX_READING = mcp.read_adc(self.adcChannel)
    #user must submerge sensor in water
    def calibrate_min(self):
        self.MIN_READING = mcp.read_adc(self.adcChannel)




    def singleRead(self):
        GPIO.output(self.pwr_pin, GPIO.HIGH)
        val = self.mcp.read_adc(self.adcChannel)
        sleep(self.dly)
        GPIO.output(self.pwr_pin, GPIO.LOW)
        moisture = ((val-self.MIN_READING)/(self.MAX_READING - self.MIN_READING))*100 #converts to percentage
        return moisture

#testing
moisture_sensor = MoistureSensor(21, 0, 7, 18)
reading = moisture_sensor.singleRead()
print(reading) # used for testing
