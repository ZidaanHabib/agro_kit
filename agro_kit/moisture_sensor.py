#import grovepi
from time import sleep
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#default and constant values:
datapin = 21 # MISO pin of pi zero
adcChannel = 7 # pin number of MCP3008  that is reading analog input
dly = 0.1 #0.1 second delay betweenr eadings by default
SPI_TYPE = 'HW'
SPI_PORT = 0 # using CE0 port on pi
SPI_DEV = 0
MAX_READING= 1
MIN_READING = 0

mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEV))


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
    val = mcp.read_adc(adcChannel)
    sleep(dly)
    moisture = ((val-MIN_READING)/(MAX_READING - MIN_READING))*100 #converts to percentage
    return moisture


singleRead()
