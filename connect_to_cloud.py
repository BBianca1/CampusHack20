# Write your code here :-)
from firebase import firebase

Akon = firebase.FirebaseApplication('https://microbit-to-database.firebaseio.com/', None)

while True:
    Acceleration = accelerometer.get_values

    data = {
    'Acc' : Acceleration
    }

    result = Akon.post('/testing/', data)
    print (result)
