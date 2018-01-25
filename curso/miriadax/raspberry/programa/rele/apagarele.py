#!/usr/bin/python3

from os import system, open, read, close, O_RDONLY
from sys import argv

directorio='/tmp/miriadax/'
archivo=directorio+'rele.state'

# open the file with the rele state // abre el fichero con el estado del rele
file=open(archivo,O_RDONLY)
# read the file with the rele state and save it in var 'state' // lee el fichero con el estado del rele y lo almacena en 'state'
state=read(file,30)
# close the file with the rele state // cierra el fichero del estado rele
close(file)

state=int(state)&int(argv[1]) # bitwise and
# with 0,1     with 0 (0000), 1( 0001), 10 (1010), 11 (1011)
# 0 & 0 > 0    0000 & 0000 > 0000  0000 & 0001 > 0000  0000 & 1010 > 0000  0000 & 1011 > 0000
# 0 & 1 > 0    0001 & 0000 > 0000  0001 & 0001 > 0001  0001 & 1010 > 0000  0001 & 1011 > 0001
# 1 & 0 > 0    1010 & 0000 > 0000  1010 & 0001 > 0000  1010 & 1010 > 1010  1010 & 1011 > 1010
# 1 & 1 > 1    1011 & 0000 > 0000  1011 & 0001 > 0001  1011 & 1010 > 1010  1011 & 1011 > 1011
state=str(state)

#store result in file archivo // almacenamos el resultado en archivo
system('echo '+ state + ' > ' + archivo)
