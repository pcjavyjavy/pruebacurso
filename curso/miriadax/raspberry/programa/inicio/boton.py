#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import os

# vars for the path and the file that we use for save the last time
# the button has been push
# directorio y fichero donde guardaremos la fecha cuando el boton fue
# puslado por ultima vez
directorio = "/tmp/miriadax/"
fichero = "boton.log"
final = 'date +"%s" >'+directorio+fichero

# pin that we use as button, in bcm // pin que usaremos para el boton, en bcm
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#forever // siempre
while True:
	input_state = GPIO.input(17) # read button
	if input_state == False: # when button is pushed // el boton ha sido pulsado
		os.system(final) # we send the command stored in 'final' to the linux system // mandamos el comando almacenado en 'final' al sistema linux
		time.sleep(0.2) # wait 200ms // esperamos 200ms
