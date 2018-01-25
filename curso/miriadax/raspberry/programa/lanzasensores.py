#!/usr/bin/python3
import http.client
import urllib.request
import urllib.parse
import json
import time
import os
import Adafruit_ADS1x15 # Import the ADS1x15 module for Analog I2C board
import Adafruit_TCS34725 # Import the TCS34725 module for Light and color sensor


# Necesary data for carriots server
# Datos necesarios para el servidor carriots 
api_url = "http://api.carriots.com/streams"
device = "RPi3@javyortega15.javyortega15"
api_key = "abcdc6e978850bf48e9dcd707e928d8e0ba653afa4e2f17005da8f06254556db"

# Temporary directory and files with the data of button, line and no line
# Directorio temporal y archivos con los datos de boton, line y no line
directorio='/tmp/miriadax/'
# The last time that button was pressed // La ultima vez que se pulso el boton
fboton=directorio+'boton.log'
# The last time that change to line was detected from IR sensor
# Ultima vez que se detecto cambio a line en el sensor IR
fline=directorio+'line.log'
# The last time that change to no line was detected from IR sensor
# Ultima vez que se detecto cambio a no line en el sensor IR
fnoline=directorio+'noline.log'

tcs = Adafruit_TCS34725.TCS34725() # We will use the TCS34725 board
adc = Adafruit_ADS1x15.ADS1015() # We will use the ADS10105 board
GAIN = 1


tcs.set_interrupt(False) # Stop interruptions // detenemos las interrupciones
# Get red, green, blue an clear from color/light sensor
# Obtenemos rojo, verde, azul y claridad del sensor de color/luz
rojo, verde, azul, claridad = tcs.get_raw_data()
# Read all the ADC values // leemos valores de la board ADC
# Read the specified ADC channel using the previously set gain value.
# Leemos el valor especifico usand la ganancia que guardamos en GAIN
# Values from 0 to 1652 // valores de resultado de 0 a 1652
# Read temperature from TMP36 analog sensor // leemos temperatura del sensor analogico TMP36
temperatura = adc.read_adc(0, gain=GAIN)
# Temperature in C from analog value // Temperatura en C a partir del valor analogico
temperatura = int(round(((temperatura*3300/1652)-500)/10))
# Read potentiometer // Leemos potenciometro
potenciometro = adc.read_adc(1,gain=GAIN)
# Potentiometer percent form analog value // Porcentaje del potenciometro a partir del valor analogico
potenciometro = int(round(potenciometro/16.52))
# Read sound from max4466 sensor // leemos sonido del sensor max4466
sonido = adc.read_adc(2,gain=GAIN)
# map value -> Minimun value 321 maximun value 1652, range=max-min=1331
# mapeado de valor -> Valor en reposo 321 maximo 1652, maximo - 321= 1331
sonido = int(round((sonido-321)/13.31))
# We have another 1 analog inputs that we can use
# Sobra 1 entrada analogica que podriamos usar
tcs.set_interrupt(True)
tcs.disable()

# Read last time button has pressed // leemos la ultima vez que se pulso el boton
file=os.open(fboton,os.O_RDONLY)
ultimoboton=os.read(file,30)
os.close(file)
ultimoboton=int(ultimoboton)

# Read last time line has detected // leemos la ultima vez que se detecto line
file=os.open(fline,os.O_RDONLY)
ultimoline=os.read(file,30)
os.close(file)
ultimoline=int(ultimoline)

# Read last time no line has detected // leemos la ultima vez que se detecto no line
file=os.open(fnoline,os.O_RDONLY)
ultimonoline=os.read(file,30)
os.close(file)
ultimonoline=int(ultimonoline)

# params and data from server // parametros y datos para el servidor
timestamp = int(time.time())

params = {"protocol": "v2",
        "device": device,
        "at": timestamp,
        "data": dict(
                temp=temperatura,
                pot=potenciometro,
                sound=sonido,
                red=rojo,
                green=verde,
                blue=azul,
                clair=claridad,
		boton=ultimoboton,
		line=ultimoline,
		noline=ultimonoline)}
binary_data = json.dumps(params).encode('ascii')

header = {"User-Agent": "raspberrycarriots",
        "Content-Type": "application/json",
        "carriots.apikey": api_key}
# Send // enviamos
req = urllib.request.Request(api_url,binary_data,header)
f = urllib.request.urlopen(req)

# confirmation // confirmacion
data=json.loads(f.read().decode('utf-8'))
print(json.dumps(data,indent=4,sort_keys=True))

