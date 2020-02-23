from microbit import *
import radio

incoming = radio.receive()

if incoming:
	#sent message to the server
