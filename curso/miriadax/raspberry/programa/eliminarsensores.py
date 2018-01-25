#! /usr/bin/python3

import json
import urllib.request
from urllib.parse import urlencode
import os
import time


# Dispositive limit
maximo = 18

# User
usuario = 'pi'


device = 'RPi3@javyortega15.javyortega15'
apikey = 'abcdc6e978850bf48e9dcd707e928d8e0ba653afa4e2f17005da8f06254556db'
params = urlencode({'sort': 'at','order':-1})
url = 'https://api.carriots.com/devices/{device}/streams/'.format(device=device)
url = url+'?'+params
headers = {
    'User-Agent': 'Raspberry-Carriots',
    'Carriots.apikey': apikey,
}
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
data=json.loads(response.read().decode('utf-8'))
totales= data['total_documents']

# a partir del siguiente al maximo vamos a eliminar
maximo+=1
# recorremos a partir del maximo permitido todos los streams para eliminarlos
for i in range(maximo,totales):
    borrar = data['result'][i]['id_developer']
    os.system('./deletemovil.py ' + borrar)
