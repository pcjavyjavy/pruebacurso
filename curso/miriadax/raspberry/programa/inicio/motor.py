#!/usr/bin/python3

from signal import pause
from gpiozero import PWMLED
import sys
import os

# we get 1 or 2 parameters // obtenemos uno o dos parametros
# one if is 0 to stop the motor // uno si es 0 para parar el motor
# two if is 1 the first to rotate left and the second the intensity from 0 to 1 // dos si es 1 para girar a la izquierda con el segundo como intensidad de 0 a 1
# two if is 2 the first to rotate right and the second the intensiti from 0 to 1 // dos si es 2 es segundo para girar a derechas y el segundo para la intensidad de 0 a 1

directorio='/tmp/miriadax/'
archivo=directorio+'motor.pid'

# we get the PID from program motor.py and store in a file. This file is the file that motor launcher use for kill this program and launch again with the new parameters // obtenemos el pid del programa motor.py para que el programa que lo lanza pueda finalizarlo y lanzarlo con los nuevos parametros
os.system('ps | grep motor.py | sed -e "s/^[ \t]*//" | cut -f1 -d" " > '+ archivo)

# pins pwm for change motor intensity // pines de valores pwm para variar la intensidad del motor
izquierda = PWMLED(13)
derecha = PWMLED(6)

if sys.argv[1] == '0': # first argument 0 -> stop // primer argumento 0 -> parada
	#print("stop")
	izquierda.value = 0.0 # stop // parada
	derecha.value = 0.0 # stop // parada
	pause()
elif sys.argv[1] == '1': # first argument 1 -> rotate left // primer argumento 1 -> girar izquierda
	#print("izquierda")
	#print(sys.argv[2])
	izquierda.value = float(sys.argv[2]) # value to rotate left second argument // valor de giro a izquierda, segundo argumento
	derecha.value = 0.0 # right-value no value because is rotating left // valor de derecha - sin valor porque esta rotando a izquiedas
	pause()
elif sys.argv[1] == '2': # first argument 2 -> rotate right // primer argumento -> girar derecha
	#print("derecha")
	#print(sys.argv[2])
	izquierda.value = 0.0 # left-value no value because is rotating right // valor izquierda, vacio, porque esta girando a la derecha
	derecha.value = float(sys.argv[2]) # value to rotate right segundo argumento
	pause()
