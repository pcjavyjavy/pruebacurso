#!/usr/bin/python3

import os
import sys

# Read the pid of the motor.py that was lauched at start and killed
# everytime you launch dcmotor.py and it lauch again with new values
# pid del programa motor.py que controla el funcionamiento del motor dc,
# se finaliza el programa y se vuelve a lanzar con los nuevos parametros
directorio='/tmp/miriadax/'
archivo=directorio +'motor.pid'
file=os.open(archivo,os.O_RDONLY)
matar=os.read(file,30)
os.close(file)

# Folder of the program // directorio del programa
basedir = os.path.dirname(os.path.abspath(__file__))


matar=int(matar)
# Kills the script // finaliza el programa
os.kill(matar,9)

# Launch again the scrip with the new values // lanza de nuevo el programa con los nuevos parametros
# first parameter = modo (0->stop, 1->forward, 2->backward)
# second parameter = velocidad(between 0->min and 1->max)
uno = sys.argv[1]
if uno != '0':
    dos = sys.argv[2]
    comando = basedir +'/inicio/motor.py ' + uno + ' ' + dos + ' &'
else:
    comando = basedir +'/inicio/motor.py 0 &'
os.system(comando)
