from microbit import *
import radio

radio.RATE_1MBIT
radio.on()
while True:
    incoming = radio.receive()

    if incoming:
        display.show(Image.HAPPY)
    # sent message to the server

    incoming = false