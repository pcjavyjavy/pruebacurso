#!/usr/bin/python3

from os import open, read, close, O_RDONLY
from gpiozero import PWMLED
from signal import pause
from time import sleep

directorio='/tmp/miriadax/'
archivo=directorio+'led.state'


#RGB led with pwm values
rojo=PWMLED(27,active_high=False)
verde=PWMLED(18,active_high=False)
azul=PWMLED(23,active_high=False)

while True:
    # open the file with the led state // abre el fichero con el estado del led
    file=open(archivo,O_RDONLY)
    # read the file with the led state and save it in var 'state'
    # lee el fichero con el estado del led y lo almacena en 'state'
    # *****
    # value is stored as 3 number from 000 to 255 for R G B
    # el valor esta almacenado en 3 numero de 000 a 255 para los valores de R G B
    for i in range(3):
        state=read(file,3) # read 3 char from file from the las position //leemos 3 caracteres del fichero desde la ultima posicion
        state=int(state) # pasamos a entero el numero
        if i==0:
            #red led value
            rojo.value=state/1020
        elif i==1:
            #green led value
            verde.value=state/1020
        else:
            azul.value=state/1020
    # close the file with the led state // cierra el fichero del estado led
    close(file)
    sleep(10)
