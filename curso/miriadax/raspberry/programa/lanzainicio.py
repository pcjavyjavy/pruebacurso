#!/usr/bin/python3

import os
# Directories and files // Directorios y archivos
directorio = "/tmp/miriadax/"
rele = directorio + "rele.state"
line = directorio + "line.log"
noline = directorio + "noline.log"
boton = directorio + "boton.log"
led = directorio + "led.state"
trabajo = directorio + "trabajo.dir"
archivolastuno = directorio + 'disp-uno.last'
archivolastdos = directorio + 'disp-dos.last'
archivolasttres = directorio + 'disp-tres.last'
archivolastcuatro = directorio + 'disp-cuatro.last'
principal = os.path.dirname(os.path.abspath(__file__))

# Default 'last' ids // Ultimas ids guardadas por defecto
lastuno = '223aaa2a3f7ef5164d4ca3928df3dd3ac9a84b11b2e507cf24a3497192aeaa4b@javyortega15.javyortega15'
lastdos = 'ae021b267356506c480aad25a7b8d429a275e4bb81e3424a7c1bdbe3e246ee9b@javyortega15.javyortega15'
lasttres = '77d3fe15dc0a8fad02b625888ff21b3351d5941040c8c580203889110c8303f1@javyortega15.javyortega15'
lastcuatro = '3ee9e7738cfb9141f36a6ab299cae39d760e104610ced1d8a75f082237890f04@javyortega15.javyortega15'

# make a termporary directory // creamos un directorio temporal
os.mkdir(directorio)
# save in this directory the next data, default value at start from rele 2 channels off 0-0
# guardamos el el lo siguiente, valor por defecto del rele de dos canales, apagados 0-0
os.system('echo 00 > ' + rele)
# the date now in boton, line and noline // la fecha actual en boton, line y noline
os.system('date +"%s" > ' + boton)
os.system('date +"%s" > ' + line)
os.system('date +"%s" > ' + noline)
# the value of the led at start RRRGGGBBB // El valor del led al iniciar RRRGGGBBB
os.system('echo 255000255 > ' + led)
# the main directory for the program // El directorio principal del programa
os.system('echo ' + principal + ' > ' +trabajo)
# start the apps in background // iniciamos las apps en segundo plano
os.system(principal + '/inicio/boton.py &') # listen button // escucha boton
os.system(principal + '/inicio/line.py &') # listen IR line and no line // escucha el sensor IR para line and no line
os.system(principal + '/inicio/motor.py 0 &') # stop dc motor // para el motor dc
os.system(principal + '/inicio/rele.py &') # drive the rele with the data in file rele // controla el rele con los datos del archivo rele
os.system(principal + '/inicio/led.py &') # drive the led with the data in file led // controla el led con los datos del archivo led
# save the last ids in files // guarda las ultimas ids en archivos
os.system('echo ' + lastuno + ' > ' + archivolastuno)
os.system('echo ' + lastdos + ' > ' + archivolastdos)
os.system('echo ' + lasttres + ' > ' + archivolasttres)
os.system('echo ' + lastcuatro + ' > ' + archivolastcuatro)
