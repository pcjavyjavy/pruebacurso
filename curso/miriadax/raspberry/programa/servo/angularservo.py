#!/usr/bin/python3

from gpiozero import AngularServo
from time import sleep
from sys import argv

pinservo=22 # bcm pin servo // pin servo bcm

#goes to a angle between 0 and 180, the angle is the parameter of the program // va a un angulo pasado como parametro al programa
#you can change the angles // puede cambiar los angulos
#the pulses must be changed for the pulses you need to get min an max angle in your servo // se deben cambiar los pulsos para su servomotor dependiendo cuales sean los pulsos de apertura maxima y minima del servo
servo = AngularServo(pinservo,min_angle=0, max_angle=180, min_pulse_width=1/2500, max_pulse_width=5/2200)

#go to angle, and wait 1 second for complete the order of change angle // va a el angulo y espera 1 segundo para que se complete la orden de cambio de angulo
servo.angle = float(argv[1])
sleep(1)

#important, wait time is neccesary for doing the order, minimun time is the time of the pulse and the time to change angle // importante, el tiempo de espera es necesario, minimo el tiempo del pulso y el tiempo de recorrido
