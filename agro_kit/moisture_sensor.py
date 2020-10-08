#import grovepi
from time import sleep
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import RPi.GPIO as GPIO
#default and constant values:
datapin = 21 # MISO pin of pi zero
adcChannel = 7 # pin number of MCP3008  that is reading analog input
dly = 0.1 #0.1 second delay betweenr eadings by default
SPI_TYPE = 'HW'
SPI_PORT = 0 # using CE0 port on pi
SPI_DEV = 0
MAX_READING= 1
MIN_READING = 0
pwr_pin = 18 # gpio pin used to power moisture sensor

GPIO.setmode(GPIO.BCM) # use broadcom pin numbering
GPIO.setup(pwr_pin, GPIO.OUT) # set pin to output mode

mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEV))

def set_pwr_pin(pin_num):
    pwr_pin = pin_num

def setDelay(delay):
    dly = delay
def setPin(pin):
    datapin = pin #set data pin to be something else if another microcontroller is used with a serial connection

def init_SPI():
    #Adafruit_GPIO allows software or hardware SPI. We are using hardware
    SPI_TYPE = 'HW'
    SPI_PORT = 0 # using CE0 port on pi
    SPI_DEV = 0

    mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEV))


#user must submerge sensor in water
def calibate_max():
    MAX_READING = mcp.read_adc(adc_channel)
#user must submerge sensor in water
def calibrate_min():
    MIN_READING = mcp.read_adc(adc_channel)




def singleRead():
    GPIO.output(pwr_pin, GPIO.HIGH)
    val = mcp.read_adc(adcChannel)
    sleep(dly)
    GPIO.output(pwr_pin, GPIO.LOW)
    moisture = ((val-MIN_READING)/(MAX_READING - MIN_READING))*100 #converts to percentage
    print(moisture) # used for testing
    return moisture


singleRead()
