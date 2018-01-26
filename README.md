# Información
*Esto es un proyecto para la prueba final del curso __Practical Internet of Things (IoT) with RaspberryPi (2 edicion)__ de [**Miriadax**](https://miriadax.net). El cual consistía en hacer programas en python que permitieran subir/bajar informacion a la nube y a su vez hacer una aplicación en android que permitiese hacer lo mismo.*

# Descripción
Mi proyecto consiste en leer varios sensores y enviar la información a la nube y controlar varios actuadores desde una aplicación de android.

Los sensores a leer son los siguientes:
- **Temperatura** leido a partir de un *sensor de temperatura* conectado a un *conversor analógico*
- **Potenciometro** leido a partir de un *potenciometro* conectado a un *conversor analógico*
- **Sonido** leido a partir de un *sensor de sonido* conectado a un *conversor analógico*
- **Color** *descompuesto en Rojo, Verde y Azul* leido a partir de un *sensor de color y luminosidad*
- **Claridad** leido a partir de un *sensor de color y luminosidad*
- **La última vez que hubo algo en un lugar concreto** leido a partir de un sensor IR
- **La última vez que dejo de haber algo en un lugar concreto** leido a partir de un *sensor IR*
- **La última pulsación de botón** leido a partir de un *botón*

Los actuadores usados son los siguientes:
- **Dos equipos conectados a 220V AC inferior a 10A** controlados a partir de un *modulo relé de dos salidas*
- **Angulo** controlado a partir de un *servo motor*
- **Motor DC** controlado a partir de un *modulo motor* o en su defecto un *arduino y un chip L293D*
- **Iluminación en un determinado color** controlado a partir de un *LED RGB*

# Materiales usados concretamente en mi caso:
*En la mayoría de los casos hay componentes más economicos que se pueden utilizar como en el caso de la tarjeta y el cargador, el cargador vale el de __casi__ cualquier smarthphone de android, incluso cualquier tarjeta micro sd que se haya quedado pequeña de un viejo smarthphone ya que se puede usar con la version sin escritorio de raspbian, es posible que tengas que usarlo con un teclado, un raton y una pantalla/televisor HDMI la primera vez que lo uses*

- [Raspberry pi **3**](https://www.amazon.es/Raspberry-Pi-Modelo-Quad-core-Cortex-A53/dp/B01CD5VC92/ref=sr_1_1?s=computers&ie=UTF8&qid=1516992365&sr=1-1&keywords=raspberry+pi+3)
- [Cargador **5V 2.1A**](https://www.amazon.es/Official-Power-Adapter-Raspberry-Pi/dp/B01CO1ELT8/ref=sr_1_2?s=computers&ie=UTF8&qid=1516992442&sr=1-2&keywords=cargador+raspberry+pi+3+oficial)
- [Tarjeta microSD **clase 10**](https://www.amazon.es/Samsung-EVO-Tarjeta-memoria-adaptador/dp/B06XW97Z9M/ref=sr_1_2?s=computers&ie=UTF8&qid=1516992531&sr=1-2&keywords=samsung+micro+sd)
- [Breadboard](http://www.cetronic.es/sqlcommerce/disenos/plantilla1/seccion/producto/DetalleProducto.jsp?idIdioma=&idTienda=93&codProducto=999441012&cPath=1017)
- Conversor Analogico Digital I2C de 12 bits de adafruit [**ADS1015**](https://www.adafruit.com/product/1083), necesita ser soldado.
- Sensor de temperatura: [**TMP36**](http://www.cetronic.es/sqlcommerce/disenos/plantilla1/seccion/producto/DetalleProducto.jsp?idIdioma=&idTienda=93&codProducto=888304007&cPath=1343)
- [Potenciometro parecido](http://www.cetronic.es/sqlcommerce/disenos/plantilla1/seccion/producto/DetalleProducto.jsp?idIdioma=&idTienda=93&codProducto=451220013&cPath=783)
- Sensor de sonido: (sin stock actualmente) [**MAX4466**](https://www.adafruit.com/product/1063) 
- Sensor de color: [**TCS34725**](https://www.adafruit.com/product/1334)
- [**Sensor IR**](https://www.pccomponentes.com/modulo-sensor-de-seguimiento-1-canal-compatible-con-arduino)
- [**Pulsador**](http://www.cetronic.es/sqlcommerce/disenos/plantilla1/seccion/producto/DetalleProducto.jsp?idIdioma=&idTienda=93&codProducto=999019247&cPath=1014)
- Controlador de motor: [**L293D**](https://www.amazon.es/Piezas-Stepper-Quadruple-Arduino-compatible/dp/B0165KHWGI/ref=sr_1_1?s=computers&ie=UTF8&qid=1516994276&sr=1-1&keywords=l293d) cada chip permite controlar dos motores dc. Trabaja a minimo 5V por lo que necesitamos tambien un **arduino** o usar en lugar del chip **L293D** un **modulo motor**
- [**Arduino Uno R3**](http://www.cetronic.es/sqlcommerce/disenos/plantilla1/seccion/producto/DetalleProducto.jsp?idIdioma=&idTienda=93&codProducto=151185017&cPath=1339)
- [Cable USB A Macho a USB B Macho parecido](http://www.cetronic.es/sqlcommerce/disenos/plantilla1/seccion/producto/DetalleProducto.jsp?idIdioma=&idTienda=93&codProducto=255369001&cPath=1294)
- [Motor DC parecido](https://www.amazon.es/20000-RPM-Motor-magnetico-velocidad/dp/B01H01PEA2/ref=sr_1_1?ie=UTF8&qid=1516995303&sr=8-1&keywords=motor+dc+9v)
- [Servo motor parecido](http://www.cetronic.es/sqlcommerce/disenos/plantilla1/seccion/producto/DetalleProducto.jsp?idIdioma=&idTienda=93&codProducto=999334074&cPath=1343)
- [LED RGB](http://www.cetronic.es/sqlcommerce/disenos/plantilla1/seccion/producto/DetalleProducto.jsp?idIdioma=&idTienda=93&codProducto=84-5A5SRBG&cPath=1158)
- [Modulo Rele](http://www.cetronic.es/sqlcommerce/disenos/plantilla1/seccion/producto/DetalleProducto.jsp?idIdioma=&idTienda=93&codProducto=888304034&cPath=1342)

# Conexiones
Dejo aquí el mapa de conexiones realizado con [**fritzing**](fritzing.org) y descargable desde el apartado [*download*](http://fritzing.org/download/).

![](https://i.imgur.com/0507fSa.png)

# Proyecto
El proyecto constaba de dos partes. Una parte consistía en crear una o varias aplicaciones en python (version 3) para controlar sensores y actuadores con la informacion de un servidor ([**carriots**](https://www.carriots.com/))  y otra en hacer una aplicacion para android con (MIT app inventor) con la información del servidor.
Por mi parte el proyecto esta dividido en varios apartados. (dentro de pruebacurso/curso/miriadax) que son las siguientes:

- **app**: Tiene la informacion de la aplicacion android.
- **fritzing**: Tiene la información de la conexión electrónica de los circuitos.
- **raspberry**: Tiene los programas en python que se ejecutarán el la raspberry

Vamos a detallar un poco más las partes.


# App
La aplicación está diseñada con [**MIT app inventor**](http://ai2.appinventor.mit.edu/) y hay que loguearse con una cuenta de google para entrar.
*La aplicacion consta de una pantalla inicial con la imagen del circuito, una breve explicacion, dos botones en los que se puede o pasar al apartado de sensores o al de actuadores y un pie en el que viene quien ha creado la aplicación.*
- Si pulsamos sobre sensores nos saldrá una pantalla en la que podremos recibir los datos del servidor [**carriots**](https://www.carriots.com/) (actualmente con mi id) o volver a la pantalla principal. Entre las opciones de visualizar los datos hay 4 botones para cambiar entre los últimos datos, la media de los datos, el maximo y el minimo.
- Si pulsamos sobre actuadores nos saldrá una pantalla en la que podremos o bien ver los últimos datos que hemos mandado desde el smarthphone al servidor **carriots** o bien ir a configuran una acción para un actuador o bien volver a la pantalla principal.
- -- Dentro de los cada pantalla de cada actuador podremos ver o los últimos datos enviados a **carriots** de ese actuador, o enviar una orden a **carriots** sobre ese actuador o volver a la pantalla de actuadores.

Dentro de este directorio estan tanto la app en formato *.apk* para poderse instalar en un smarthphone, como en formato *.aia* para poderla cambiar en [*MIT app inventor*](http://ai2.appinventor.mit.edu/) y así poder poner **sus** propios ids de carriots.

# Fritzing
Aquí están los planos del circuito tanto en formato *.fzz* que es el utilizado por [*fritzing*](fritzing.org) como en formato imagen *.png* y vectorial *.svg* y tambien la lista de materiales en formato *.html*

# Raspberry
Aquí están las aplicaciones divididas en tres apartados con dos readme uno en 'ingles' y otro en castellano que tienen toda la información de las divisiones.
Aún así se explicaran aquí.
- **instalacion** tiene un ejecutable que se encarga de obtener las librerias necesarias para el correcto funcionamiento de los programas (partiendo de la instalacion de raspbian version Noviembre 2017 del 29/11/2017)
- **programa** tiene todos los ficheros ejecutables divididos en partes para que funciones cada uno de los modulos, está dividido en varios apartados.
- **automatizacion** tiene un ejecutable que crea una *NUEVA* tabla de crontab para el usuario que lo ejecuta con los programas principales que han de lanzarse para que todo esté en funcionamiento.
