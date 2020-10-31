
import gps
import moisture_sensor
from time import sleep
import light_sensor
import agro_kit as ag


def setup():
    global exit
    exit = False
    print("Welcome to the Demo. This a basic overview of some of the functions in our API\n" )# WElcome message
    global myAG
    myAG = ag.AgroKit()


def main():
    global exit# use global exit var
    global myAG
    options = "1) Read Moisture\n2) Read Lux\n3) Read GPS RMC Message\nq) exit"
    print(options)
    cmd = input("\nEnter a command:\n")
    print("\n")
    if cmd == '1':
        myAG.MS.singleRead()
    elif cmd == '2':
        light_sensor = myAG.LS.singleReadLux()
        print("Lux: " + str(light))
    elif cmd == '3':
        print(myAG.GPS.getRMC())
    else:
        exit = True



if __name__ == "__main__":
    setup()
    while not exit:
        main()
        sleep(0.2)
        print("\n")
