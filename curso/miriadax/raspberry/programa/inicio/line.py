#!/usr/bin/python3
import os
from gpiozero import LineSensor
from signal import pause

# script that uses gpiozero library with the LineSensor 'drivers' and
# functions
# when IR sensor detect somethig between the sensor and her range we save the
# time in line.log
# when IR sensor no detect something between the sensor and her range we save
# the time in noline.log

# este programa usa la libreria gpiozero que usa unas funciones especificas
# para el sensor IR
# cuando el sensor IR detecta que hay algo entre el y su rango de deteccion
# guarda la fecha en line.log
# cuando el sensor detecta que ha dejado de haber algo entre el sensor
# y su rango de alcance guarda la fecha en noline.log

directorio = "/tmp/miriadax/"

sensor = LineSensor(26)
sensor.when_line = lambda: os.system('date +"%s" > '+directorio+'/line.log')
sensor.when_no_line = lambda: os.system('date +"%s" >'+directorio+ '/noline.log')
pause() # it wait for another signal from sensor // se mantiene a la espera de otra señal del sensor
