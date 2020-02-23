#Main device program
from microbit import *
import random
import radio

while True:
    sleep(20)
    if abs(accelerometer.get_x()) > 1500 and abs(accelerometer.get_y()) > 1500:
        if abs(accelerometer.get_z()) > 1500:
         	radio.on()
		radio.send("ALERT!")
		radio.off()
