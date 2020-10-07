# Light Sensor 

# Package import
import time

import board
import busio

import adafruit_tcs34725
import RPi.GPIO as GPIO 

# Initialize bus and constants.
# Decision to power on sensor only when function is called in order to conserve energy

def powerUp():
    GPIO.setmode(GPIO.BCM) # GPIO PIN 17 to power sensor
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, 1) 


i2cbus = busio.I2C(board.SCL, board.SDA)
light_sensor = adafruit_tcs34725.TCS34725(i2cbus)
sample_rate = 5
temp = light_sensor.color_temperature
lux = light_sensor.lux
time.sleep(0.5)  # allow for led to illuminate environment for accuracy

# While loop to read and display sensor data
def loopRead():
    powerUp()
    while True:
     
        temp = light_sensor.color_temperature
        lux = light_sensor.lux
        print("Temperature: {0}K Lux: {1}".format(temp, lux))
    # Sample rate for loop
        time.sleep(sample_rate)
    return temp + lux 

# Function to read colour and luminosity
def readColourLux():
    powerUp()
    temp = light_sensor.color_temperature
    lux = light_sensor.lux
    print("Temperature: {0}K Lux: {1}".format(temp, lux))
    return temp + lux 

# Function to read luminosity
def lux():
    powerUp()
    lux = light_sensor.lux
    print("Lux: {1}".format(temp, lux))
    return lux 

# Function to read colour # Could be used for plant health? Green/Brown
def colour():
    powerUp()
    colour = light_sensor.color_temperature
    print("Temperature: {0}K".format(temp))
    return lux 

# Function to read individual colours
def RGB():
    powerUp()
    print('Color: (Red {0}, Green {1}, Blue {2})'.format(*light_sensor.color_rgb_bytes))

# Set Sample Rate
def setSampleRate(Rate):
    sample_rate = rate

# Calibrate light sensor for daylight
def sunlight():
    powerUp()
    sunset = light_sensor.lux

# Calibrate light sensor for dark
def sunset():
    powerUp()
    sunset = light_sensor.lux

colour()
lux()

readColourLux()
RGB()
GPIO.output(17, 0) # remove power from sensor