#! /usr/bin/python3

import json
import urllib.request
from urllib.parse import urlencode
import os
import time


# ********************************************************************
# ********************************************************************
# ********************************************************************
#                declaracion de variables                            *
# ********************************************************************
# ********************************************************************
# ********************************************************************

# Dispositive limit
maxdispositivo = 150

# User, we don't need now
usuario = ''

# Directories
dirtemporal ='/tmp/miriadax/'
basedir = os.path.dirname(os.path.abspath(__file__))
os.chdir(basedir)
os.chdir('..')
basedir=os.getcwd()
rutacron = basedir + '/crontab'
dirtrabajo= dirtemporal + 'trabajo.dir'
dirrele = dirtemporal + 'rele.state'
dirled = dirtemporal + 'led.state'
archivolastuno = dirtemporal + 'disp-uno.last'
archivolastdos = dirtemporal + 'disp-dos.last'
archivolasttres = dirtemporal + 'disp-tres.last'
archivolastcuatro = dirtemporal + 'disp-cuatro.last'

file=os.open(dirtrabajo,os.O_RDONLY)
trabajo=os.read(file,30)
os.close(file)

trabajo=str(str(trabajo)[2:])[:-3]


# Data for carriots server // Datos para el servidor carriots
device = 'Movil@javyortega15.javyortega15'
apikey = 'abcdc6e978850bf48e9dcd707e928d8e0ba653afa4e2f17005da8f06254556db'
params = urlencode({'sort': 'at','order':-1})
url = 'https://api.carriots.com/devices/{device}/streams/'.format(device=device)
url = url+'?'+params
headers = {
    'User-Agent': 'Raspberry-Carriots',
    'Carriots.apikey': apikey,
}
# send request // envio peticion
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)

# return data // datos recibidos
data=json.loads(response.read().decode('utf-8'))

# all streams // todos los streams
totales= data['total_documents']


# contadores de cada tipo
# uno = motordc, dos= servo, tres=led, cuatro =rele
unos = 0
doses = 0
treses = 0
cuatros = 0

# si hay o no valores de ultimos led y motor dc solo usado para valores de poner lo antes posible
firstled = True
firstdc = True

# orden en que se ejecutaran las ultimas ordenes de los servos y reles programadas
ordenesservo = {}
ultimoservo=0
ordenesrele ={}
ultimorele=0
relelaststate=0


# si hay ya un valor ultimo encontrado
yalastuno = False
yalastdos = False
yalasttres = False
yalastcuatro = False


# ids de los ultimos valores
lastuno = '223aaa2a3f7ef5164d4ca3928df3dd3ac9a84b11b2e507cf24a3497192aeaa4b@javyortega15.javyortega15'
lastdos = 'ae021b267356506c480aad25a7b8d429a275e4bb81e3424a7c1bdbe3e246ee9b@javyortega15.javyortega15'
lasttres = '77d3fe15dc0a8fad02b625888ff21b3351d5941040c8c580203889110c8303f1@javyortega15.javyortega15'
lastcuatro = '3ee9e7738cfb9141f36a6ab299cae39d760e104610ced1d8a75f082237890f04@javyortega15.javyortega15'


# ids de los primeros valores
firstuno = ''
firstdos = ''
firsttres = ''
firstcuatro = ''


#valores que tendran los dispositivos al ser leidos
mes = ''
dia = ''
hora = ''
minuto = ''
red = '0'
green = '0'
blue = '0'
tipo = ''
valor = ''
#id a borrar
borrar = ''
programa = ''


# id guardados en fichero de las ultimas ordenes procesadas
file=os.open(archivolastuno,os.O_RDONLY)
lastuno=os.read(file,300)
os.close(file)
file=os.open(archivolastdos,os.O_RDONLY)
lastdos=os.read(file,300)
os.close(file)
file=os.open(archivolasttres,os.O_RDONLY)
lasttres=os.read(file,300)
os.close(file)
file=os.open(archivolastcuatro,os.O_RDONLY)
lastcuatro=os.read(file,300)
os.close(file)

# necesitamos quitar ciertos caracteres al no ser leido como str
lastuno=str(str(lastuno)[2:])[:-3]
lastdos=str(str(lastdos)[2:])[:-3]
lasttres=str(str(lasttres)[2:])[:-3]
lastcuatro=str(str(lastcuatro)[2:])[:-3]



# ************************************************************************
# ************************************************************************
# ************************************************************************
#                     fin declaracion de variables                       *
# ************************************************************************
# ************************************************************************
# ************************************************************************




# recorremos todos los valores de todos los dispositivos
for i in range(totales):

    # ********************************************************************
    #                                                                    *
    # con try-except comprobamos que la lectura del dato sea correcta    *
    #                                                                    *
    #                                                                    *
    # ********************************************************************

    # ********************************************************************
    #                                                                    *
    #                     lectura de datos genericos                     *
    #                                                                    *
    # ********************************************************************

    try:
        dispositivo = int(data['result'][i]['data']['Dispositivo'])
    except:
        dispositivo = 0
        borrar = data['result'][i]['id_developer']
        os.system(basedir + '/programa/deletemovil.py ' + borrar)
    id = data['result'][i]['id_developer']
    try:
        mes = data['result'][i]['data']['Mes']
    except:
        borrar = data['result'][i]['id_developer']
        os.system(basedir + '/programa/deletemovil.py ' + borrar)
    try:
        dia = data['result'][i]['data']['Dia']
    except:
        borrar = data['result'][i]['id_developer']
        os.system(basedir + '/programa/deletemovil.py ' + borrar)
    try:
        hora = data['result'][i]['data']['Hora']
    except:
        borrar = data['result'][i]['id_developer']
        os.system(basedir + '/programa/deletemovil.py ' + borrar)
    try:
        minuto = data['result'][i]['data']['Minuto']
    except:
        borrar = data['result'][i]['id_developer']
        os.system(basedir + '/programa/deletemovil.py ' + borrar)


    # ***********************************************************************
    # ***********************************************************************
    #                   fin lectura valores genericos                       *
    # ***********************************************************************
    # ***********************************************************************

    # ***********************************************************************
    # ***********************************************************************
    # Actuators that aren't led rgb (other generic values)                  *
    # Dispositivos distintos a led (otros valores menos genericos)          *
    # if the data is corrupt we will delete the line                        *
    # ***********************************************************************
    # ***********************************************************************

    if dispositivo<3 or dispositivo == 4:
        try:
            tipo = data['result'][i]['data']['Tipo']
        except:
            borrar = data['result'][i]['id_developer']
            os.system(basedir + '/programa/deletemovil.py ' + borrar)
        try:
            valor = data['result'][i]['data']['Valor']
        except:
            borrar = data['result'][i]['id_developer']
            os.system(basedir + '/programa/deletemovil.py ' + borrar)


        # *******************************************************************
        # Dispositivo 1 (MOTOR DC)                                          *
        # EN:                                                               *
        # In this part, if we have the first actuator we are going to do:   *
        # 1- If is the first DCMotor of this this running program           *
        #    we'll get the id. At the end of the program we save this id    *
        #    and we use this id in the next run of the program              *
        # 2- Change the number of the DCMotor line                          *
        # 3- If the if is NOT the same as the first id read in the last     *
        #    run of this program and we didn't find the last id yet         *
        #    we'll run the orders depending if we have to run now or later  *
        # 4- If 'date' have '99' we run now, because in the phone app we    *
        #    use 99 for defining that we have to do it as soon as possible  *
        #  - If we have other 'date' we send it to the cron file to with    *
        #    the date to run when the date arrives                          *
        # 5- If we get the maximun number of lines of actuator we delete    *
        #    the next old lines                                             *
        # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
        # ES:                                                               *
        # En esta parte, si estamos con el primer dispositivo haremos:      *
        # 1- Si es la primera DCMotor desde que ejecutamos el programa      *
        #    obtendremos el id. Al final del programa lo guardaremos        *
        #    y lo usaremos en la siguiente ejecucion del programa.          *
        # 2- Cambiar el numero de entrada de motor DC                       *
        # 3- Si NO coincide el id con el primero del programa anterior      *
        #    y ademas no hemos encontrado la coincidencia aun               *
        #    ejecutaremos las ordenes dependiendo si hay que ejecutarlo     *
        #    ahora o bien mas adelante                                      *
        # 4- Si esta fechado con 99 lo correremos ahora porque el la app    *
        #    usamos 99 para decir que se habia elegido "lo antes posible"   *
        #  - Si tenemos otra fecha se almacenara el el fichero cron         *
        #    y este es encargara de ejecutarlo cuando llegue el momento     *
        # 5- Si tenemos el maximo numero entradas sobre este dispositivo    *
        #    borraremos las entradas antiguas                               *
        # *******************************************************************

        if dispositivo==1:
            if unos == 0:
                firstuno = id
            unos+=1
            if id == lastuno:
                yalastuno = True
            if id != lastuno and yalastuno == False:
                valor=int(valor)/100
                if dia == 99 and mes == 99:
                    if hora == 99 and minuto == 99:
                        # os.system run a system program like we run in the console//os.system lanza un programa como si lo hiciesemos desde la consola
                        # dcmotor.py is the program and tipo(as string) and valor (as string) the arguments // dcmotor.py es el programa y tipo(como cadena) y valor(como cadena) los parametros
                        os.system(basedir + '/programa/dcmotor.py '+ str(tipo) + ' ' + str(valor) + ' &')
                    else:
                        # here we use echo with the string we echoes and redirect the output to append to the cron file // aqui usamos echo con la cadena que queremos sacar y redireccionamos la salida para añadirsela a el fichero de cron
                        os.system('echo '+ str(minuto) +' ' + str(hora) + ' ' + str(time.localtime().tm_mday) + ' ' + str(time.localtime().tm_mon) + ' \* ' + usuario + ' ' + str(trabajo)  + '/dcmotor.py ' + str(tipo) + ' ' +str(valor) + '\& >> ' + rutacron)
                else:
                    os.system('echo '+ str(minuto) +' ' + str(hora) + ' ' + str(dia) + ' ' + str(mes) + ' \* ' + usuario + ' ' + str(trabajo)  + '/dcmotor.py ' + str(tipo) + ' ' + str(valor) + '\& >> ' + rutacron)
            if unos > maxdispositivo:
                eliminar=data['result'][i]['id_developer']
                os.system('./deletemovil.py ' + eliminar)
                unos-=1

        # **********************************************************************
        # Dispositivo 2 (Servo)                                                *
        # EN: Like DCMotor                                                     *
        # Changes:                                                             *
        #   We use 2 programs depending if we send a angle to the Servo or     *
        #     we use a time to open and close.                                 *
        #   We store the 'now' orders in a diccionary and we run from old to   *
        #     new at the end of the program                                    *
        # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
        # ES: Como MotorDC                                                     *
        # Cambios:                                                             *
        #   Usamos 2 programas dependiendo de si mandamos el angulo al servo   *
        #     o el tiempo de apertura y cierre                                 *
        #   Almacenamos las ordenes que hay que hacer lo mas rapido posible en *
        #     un diccionario para ejecutarlas de vieja a nueva al final        *
        # **********************************************************************

        elif dispositivo==2:
            if doses == 0:
                firstdos=id
            doses+=1
            if id == lastdos:
                yalastdos = True
            if id != lastdos and yalastdos == False:
                if tipo == 1:
                    programa = basedir + '/programa/servo/abrirycerrar.py'
                elif tipo == 2:
                    programa = basedir + '/programa/servo/angularservo.py'
                if dia == 99 and mes == 99:
                    if hora == 99 and minuto == 99:
                        ordenesservo[ultimoservo]=[tipo,valor]
                        ultimoservo+=1
                    else:
                        os.system('echo '+ str(minuto) +' ' + str(hora) + ' ' + str(time.localtime().tm_mday) + ' ' + str(time.localtime().tm_mon) + ' \* ' + usuario + ' ' + programa + ' ' + str(valor) + ' \& >> ' + rutacron)
                else:
                    os.system('echo '+ str(minuto) +' ' + str(hora) + ' ' + str(dia) + ' ' + str(mes) + ' \* ' + usuario + ' ' + programa + ' ' + str(valor) + ' \& >> ' + rutacron)
            if doses > maxdispositivo:
                eliminar=data['result'][i]['id_developer']
                os.system(basedir + '/programa/deletemovil.py ' + eliminar)
                doses-=1

        # **********************************************************************
        # Dispositivo 4 (Rele)                                                 *
        # EN:                                                                  *
	# The same as Servo, but it uses 3 programs instead of 2, one for      *
        # put on the channels of the rele thas we send 'ON', one for put off   *
        # the channels of the rele that we send 'OFF' and one for put the      *
        # the channels like we want instead of its last state                  *
        # ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
        # ES:                                                                  *
        # Igual que el Servo pero usa 3 programas en lugar de dos, uno para    *
        # encender los canales que se mandaron encender, otra para apagar los  *
        # que se mandaron apagar y otro para ponerlos como se quiera en ese    *
        # momento independientemente de como esten                             *
        # **********************************************************************

        elif dispositivo==4:
            if cuatros == 0:
                firstcuatro=id
            if id == lastcuatro:
                yalastcuatro = True
            cuatros+=1
            if id != lastcuatro and yalastcuatro == False:
                if tipo == 1:
                    programa = basedir + '/programa/rele/encienderele.py'
                elif tipo == 2:
                    programa = basedir + '/programa/rele/apagarele.py'
                elif tipo ==3:
                    programa = basedir + '/programa/rele/ponrele.py'
                if dia == 99 and mes == 99:
                    if hora == 99 and minuto == 99:
                        ordenesrele[ultimorele]=[tipo,valor]
                        ultimorele+=1
                    else:
                        os.system('echo '+ str(minuto) +' ' + str(hora) + ' ' + str(time.localtime().tm_mday) + ' ' + str(time.localtime().tm_mon) + ' \* ' + usuario + ' ' + programa + ' ' + str(valor) + ' \& >> ' + rutacron)
                else:
                    os.system('echo '+ str(minuto) +' ' + str(hora) + ' ' + str(dia) + ' ' + str(mes) + ' \* ' + usuario + ' ' + programa + ' ' + str(valor) + ' \& >> ' + rutacron)
            if cuatros > maxdispositivo:
                eliminar=data['result'][i]['id_developer']
                os.system(basedir + '/programa/deletemovil.py ' + eliminar)
                cuatros-=1


    # **************************************************************************
    # **************************************************************************
    # Dispositivo 3 (LED RGB)                                                  *
    # **************************************************************************
    # **************************************************************************

    # **************************************************************************
    # EN:                                                                      *
    # We read others values that use in this part instead of tipe and value    *
    #   There are RED, GREEN and BLUE to compose a color for the led           *
    # Instead of run a program we save it in a file, and a program read the    *
    #   file from time to time.                                                *
    # Only use the last 'now' value, the values from cron are like in other    *
    #   parts.                                                                 *
    # ** ** ** ** ** ** ** ** ** ** **  ** ** ** ** ** ** ** ** ** ** ** ** ** *
    # ES:                                                                      *
    # Leemos los otros valores que se usan es esta parte en lugar de los de    *
    #   tipo y valor usados anteriormente usamos, ROJO, VERDE y AZUL para crear*
    #   el color del led.                                                      *
    # En lugar de ejecutar un programa guardamos en un fichero el valor de los *
    #   colores de los leds y un programa se encarga de leerlos de tiempo en   *
    #   tiempo.                                                                *
    # Solo usamos el ultimo valor 'lo mas rapido posible', los otros valores   *
    #   son guardados para cron como en cualquier otro apartado                *
    # **************************************************************************

    if dispositivo==3:
        try:
            red = data['result'][i]['data']['Red']
        except:
            borrar = data['result'][i]['id_developer']
            os.system(basedir + '/programa/deletemovil.py ' + borrar)
        try:
            green = data['result'][i]['data']['Green']
        except:
            borrar = data['result'][i]['id_developer']
            os.system(basedir + '/programa/deletemovil.py ' + borrar)
        try:
            blue = data['result'][i]['data']['Blue']
        except:
            borrar = data['result'][i]['id_developer']
            os.system(basedir + '/programa/deletemovil.py ' + borrar)
        if treses == 0:
            firsttres = id
        treses+=1
        if id == lasttres:
            yalasttres = True
        # Put 0s at left to store in a file because we will read from 3 to 3 chars
        # Rellenamos con 0s a la izquierda para ser leidos de 3 en 3
        if id != lasttres and yalasttres==False:
            if int(red) < 10:
                red = '00' + str(int(red))
                print(red)
            elif int(red) < 100:
                red = '0' + str(int(red))
                print(red)
            if int(green) < 10:
                green = '00' + str(int(green))
                print(green)
            elif int(green) < 100:
                green = '0' + str(int(green))
                print(green)
            if int(blue) < 10:
                blue = '00' + str(int(blue))
                print(blue)
            elif int(blue) < 100:
                blue = '0' + str(int(blue))
                print(blue)
            if dia == 99 and mes == 99:
                if hora == 99 and minuto == 99:
                    print('actual ' + str(red) + str(green) + str(blue))
                    if firstled == True:
                        os.system('echo '+ str(red) + str(green) + str(blue) + ' > ' + dirled)
                        firstled = False
                else:
                    print('hoy ' + str(red) + str(green) + str(blue))
                    os.system('echo '+ str(minuto) +' ' + str(hora) + ' ' + str(time.localtime().tm_mday) + ' ' + str(time.localtime().tm_mon) + ' \* ' + usuario + ' /bin/echo '+ str(red) + str(green) + str(blue) + ' \> ' + dirled + ' >> ' + rutacron)
            else:
                print('otro ' + str(red) + str(green) + str(blue))
                os.system('echo '+ str(minuto) +' ' + str(hora) + ' ' + str(dia) + ' ' + str(mes) + ' \* ' + usuario + ' /bin/echo '+ str(red) + str(green) + str(blue) + ' \> ' + dirled + ' >> ' +  rutacron)
        if treses > maxdispositivo:
            eliminar=data['result'][i]['id_developer']
            os.system(basedir + '/programa/deletemovil.py ' + eliminar)
            treses-=1


# Put values in screen
print('Totales: ' + str(totales))
print('Motor DC: '+str(unos))
print('Servo Motor: '+str(doses))
print('LED RGB: '+str(treses))
print('Rele: '+str(cuatros))

# Update crontab
os.system('crontab ' + rutacron)

# Update rele 'now' values
# A program read the rele values from a file
# We read the file and change the values
ultimorele-=2
file=os.open(dirrele,os.O_RDONLY)
relelaststate=os.read(file,30)
os.close(file)
relelaststate=int(relelaststate)

for i in range(ultimorele,-1,-1):
    tipo=ordenesrele[i][0]
    valor=ordenesrele[i][1]
    if tipo == 1:
        relelaststate=relelaststate|valor
    elif tipo == 2:
        relelaststate=relelaststate&valor
    elif tipo == 3:
        relelaststate=valor
os.system(basedir + '/programa/rele/ponrele.py ' + str(relelaststate) + ' &')


# Update servo 'now' values
# We run the servo program with values
ultimoservo-=2
print("Ordenes Servo")
for i in range(ultimoservo,-1,-1):
    tipo=ordenesservo[i][0]
    valor=ordenesservo[i][1]
    if tipo == 1:
        print('Abrir...')
        os.system(basedir + '/programa/servo/abrirycerrar.py ' + str(valor))
        print('Realizado')
    elif tipo == 2:
        print('Posicion...')
        os.system(basedir + '/programa/servo/angularservo.py ' + str(valor))
        print('Realizado')


# Update last values
os.system('echo ' + str(firstuno) + ' > ' + archivolastuno)
os.system('echo ' + str(firstdos) + ' > ' + archivolastdos)
os.system('echo ' + str(firsttres) + ' > ' + archivolasttres)
os.system('echo ' + str(firstcuatro) + ' > ' + archivolastcuatro)
