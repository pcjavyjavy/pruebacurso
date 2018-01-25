#!/usr/bin/python3

import os

# Here we use 'os' library to operate with linux os system
# Aqui usamos la libreria 'os' para trabajar con el sistema operativo linux
# Get the user // obtenemos el usuario
usuario=os.getlogin()
# Go to parent directory // Vamos al directorio superior
os.chdir('..')
# Get the absolute path // Obtenemos el directorio absoluto
directorio=os.getcwd()
# Save the lines to a file to schedule it
# Guardamos las lineas en un fichero para hacer un organizador de tareas
os.system('echo \*/1 \* \* \* \* ' + directorio + '/programa/hayinicio.py \& > ' + directorio + '/crontab')
os.system('echo \*/10 \* \* \* \* ' + directorio + '/programa/lanzasensores.py \& >> ' + directorio + '/crontab')
os.system('echo \*/10 \* \* \* \* ' + directorio + '/programa/sacarmovil.py \& >> ' + directorio + '/crontab')
os.system('echo 33 3 \* \* \* ' + directorio + '/programa/eliminasensores.py \& >> ' + directorio + '/crontab')
# Set file as schedule for the os // Establecemos el archovo como horario de tareas
os.system('crontab ' + directorio + '/crontab')
# Set exec to the python files to avoid problems
# Hacemos ejecutables los ficheros python para evitar problemas
os.system("find . -type f -name '*.py' -exec chmod u+x {} \;")
