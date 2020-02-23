from microbit import *
import radio

incoming = radio.receive()

if incoming:
	display.show(Image.HAPPY)
	#sent message to the server
