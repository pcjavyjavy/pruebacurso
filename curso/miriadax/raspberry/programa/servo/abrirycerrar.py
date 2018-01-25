#!/usr/bin/python3

from gpiozero import Servo
from time import sleep
from sys import argv

pinservo = 22 #pin bcm servo // pin bcm del servo

# open a maximun angle a number of second received as parameter // abre al angulo maximo durante un tiempo en segundos pasado como parametro
# aprox min pulse and max pulse of servo, it must be changed depends of your servo // min pulse y max pulse en segundos aproximado, cambiese por los de su servo
servo = Servo(pinservo,min_pulse_width=1/2500, max_pulse_width=5/2200)

servo.max() # servo -> maximun angle  // servo -> angulo maximo
if argv[1]: # parameter 1 // parametro 1
	tiempo = float(argv[1]) # change string to float of first parameter // pasamos a float el primer parametro
	if tiempo > 0: # if time greater than 0 go to minimun angle, else it will be at maximun angle and not change in this program // si el tiempo es mayor que 0 , esperamos ese tiempo y pasamos al minimo angulo, sino dejamos el anuglo tal cual
		sleep(tiempo) # wait time // esperamos ese tiempo
		servo.min() # servo -> minimun angle // servo -> angulo minimo
		sleep(1) #wait 1 second, if we don't wait the program don't do the change of position // esperamos 1 segundo, sino esperamos el servo no se mueve
#important, sleep time must be at least the time that the pulse is send and the necesary time to change position // importante, el tiempo de espera debe ser de al menos el tiempo que tarda en enviarse el pulso y el tiempo que tarda en cambiar de posicion
