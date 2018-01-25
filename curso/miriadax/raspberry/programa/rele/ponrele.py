#!/usr/bin/python3

from os import system, open, read, close, O_RDONLY
from sys import argv

directorio='/tmp/miriadax/'
archivo=directorio+'rele.state'

#store the new input in archivo // almacenamos la nueva entrada en archivo
system('echo '+ argv[1] + ' > ' + archivo)
