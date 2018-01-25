#!/usr/bin/python3

from os import open, read, close, O_RDONLY
from time import sleep
from gpiozero import LED

# where read the value of rele // archivo para leer el estado del rele
directorio='/tmp/miriadax/'
archivo=directorio+'rele.state'

# rele pins // pines de los reles
rele1=LED(5)
rele2=LED(16)

# forever // siempre
while True:
	# open file as read only // abrimos archivo como solo lectura
	file=open(archivo,O_RDONLY)
	# read 30 characters // leemos hasta 30 caracteres
	state=read(file,30)
	# close file // cerramos fichero
	close(file)
	# transform str to int // pasamos de str a int
	state=int(state)
	# depends of the number we put the reles // ponemos los reles segun el numero
	if state == 0:
		rele1.off()
		rele2.off()
	elif state == 1:
		rele1.on()
		rele2.off()
	elif state == 10:
		rele1.off()
		rele2.on()
	else:
		rele1.on()
		rele2.on()
	sleep(10)
