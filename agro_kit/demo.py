
import gps
import moisture_sensor
from time import sleep
import light_sensor
import agro_kit as ag
import os


def setup():
    global exit
    exit = False
    print("Welcome to the Demo. This a basic overview of some of the functionality in our API.\n" )# Welcome message
    global myAG
    myAG = ag.AgroKit()


def main():
    global exit# use global exit var
    global myAG
    options = '''1) Read Moisture\n2) Read Lux\n3) Read GPS RMC Message \
    \n4) Full Read \n5) Create profile\n6) Load profile\n7) Full Read and check within range \nq) exit'''
    print(options)
    cmd = input("\nEnter a command:\n")
    print("\n")
    if cmd == '1':
        print("Moisture: "+  str(myAG.MS.singleRead()))
    elif cmd == '2':
        light = myAG.LS.singleReadLux()
        print("Lux: " + str(light))
    elif cmd == '3':
        print(myAG.GPS.getRMC())
    elif cmd == '4':
        myAG.read()
    elif cmd == '5':
        name = input("Enter a profile name:\n")
        minMoist = eval(input("Enter min moisture:\n"))
        maxMoist = eval(input("Enter max moisture:\n"))
        minLux = eval(input("Enter min lux:\n"))
        maxLux = eval(input("Enter max lux:\n"))
        ag.createProfile(name, minMoist, maxMoist, minLux, maxLux)
    elif cmd == '6':
        name = input("Enter profile name to load:\n")
        myAG.loadProfile(name)
        print('Min Moisture: ' + str(myAG.MIN_MOISTURE) + "\tMax Moisture: " + str(myAG.MAX_MOISTURE)\
        + "\tMin Lux: " + str(myAG.MIN_LUX) + "\tMax Lux: " + str(myAG.MAX_LUX))
    elif cmd == '7':
        reading = myAG.read()
        msg = ['']
        ok = myAG.readingOK(reading, msg)
        print(msg[0])
    else:
        exit = True



if __name__ == "__main__":
    setup()
    while not exit:
        main()
        sleep(0.2)
        print("\n")
