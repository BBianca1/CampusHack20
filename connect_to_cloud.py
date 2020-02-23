# Write your code here :-)
from microbit import *
from firebase import firebase

import radio

radio.on()

Akon = firebase.FirebaseApplication('https://microbit-to-database.firebaseio.com/', None)

while True:
    Acceleration = accelerometer.get_x()

    data = {
    'Acc' : Acceleration
    }

    result = Akon.post('/testing/', data)
    print (result)
