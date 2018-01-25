#!/usr/bin/python3

import http.client
import urllib.request
import urllib.parse
import json
from sys import argv

# Deletes a stream from carriots. Stream is an argument.
# Elimina un stream de carriots el cual es pasado como argumento
api_url = "http://api.carriots.com/streams/"+argv[1]+"/"
api_key = "abcdc6e978850bf48e9dcd707e928d8e0ba653afa4e2f17005da8f06254556db"

# No params // sin parametros
params = {}
binary_data = json.dumps(params).encode('ascii')

# Header // cabecera
header = {"carriots.apikey": api_key}

# Request // solicitud
req = urllib.request.Request(api_url,binary_data,header)
req.get_method = lambda: "DELETE"
f = urllib.request.urlopen(req)

# Decode the received data // decodificamos los datos obtenidos
data=json.loads(f.read().decode('utf-8'))
# If was deleted it get a message. In the deleted case we print on screen the
# id string before '@'
# Si se ha eliminado devolvera un mensaje. En caso de ser eliminado mostraremos
# por pantalla el la parte del id hasta la '@'
eliminado=data['message']
if eliminado == "Stream deleted":
    eliminado = 'Eliminado ' + argv[1].split('@')[0]
    print(eliminado)
