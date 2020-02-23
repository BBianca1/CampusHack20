# Write your code here :-)
from microbit import *
import random

# import serial

# for i in range(1000):
while True:
    sleep(20)
    if abs(accelerometer.get_x()) > 1500 and abs(accelerometer.get_y()) > 1500:
        if abs(accelerometer.get_z()) > 1500:
            # base_heart_rate = 80 + random.randint(-200, 201)
            # if abs(base_heart_rate) > 140 and abs(base_heart_rate) < 80:
            print("ALERT")
