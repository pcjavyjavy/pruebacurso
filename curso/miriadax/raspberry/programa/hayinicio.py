#!/usr/bin/python3

import os

# Temporal folder // Directorio temporal
temporal='/tmp/miriadax'
# The folder of the program // Directorio del programa
basedir = os.path.dirname(os.path.abspath(__file__))
# Look if the folder exists // Miramos si existe el directorio
resultado = os.path.exists(temporal)
# Program that we launch if didn't exist // programa que lanzaremos si no existe
programa= basedir + '/lanzainicio.py'


# If doesn't exists lauch the program // Si no existe lanzamos el programa
if resultado == False:
    os.system(programa)
