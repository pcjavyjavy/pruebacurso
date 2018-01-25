#!/usr/bin/python3

import os

# Here we use 'os' library to operate with linux os system
# Aqui usamos la libreria 'os' para trabajar con el sistema operativo linux

# Get the list of the last packages and install the packages we need from os
# and form python, and libraries from our sensors
# Obtenemos la lista de los paquetes e instalamos los paquetes que necesitamos
# oara es sistema operativo y para python, y las librerias de nuestros sensores
os.system('sudo apt-get update')
os.system('sudo apt-get install -y python3 python3-pip python-dev')
os.system('sudo pip3 install rpi.gpio')
os.system('sudo pip install adafruit-ads1x15')
os.system('sudo pip install adafruit-tcs34725')
