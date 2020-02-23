# Main device program
from microbit import *
# import random
import radio

radio.RATE_1MBIT

while True:
    sleep(20)
    if abs(accelerometer.get_x()) > 1500 and abs(accelerometer.get_y()) > 1500:
        if abs(accelerometer.get_z()) > 1500:
            print("ALERT")
            radio.on()
            radio.send("ALERT!")
            sleep(50)

            incoming = radio.receive()

            if incoming:
                display.show(Image.HAPPY)
            radio.off()
            sleep(50)