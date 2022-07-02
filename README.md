# Proyecto-Digital-II

Integrantes:
- Ana Maria Quintero Leon
- Diana Patricia Cortes Nava


### Introducción

Este repositorio contiene la entrega final del proyecto de la materia Electrónica Digital II de la Universidad Nacional de Colombia, realizado en Litex. La propuesta del proyecto consiste en un sistema de cajeros ecológicos, el cual realiza la separación de 3 tipos de residuos (Plástico, metal y papel), esto mediante sensores que ayudan a detectar el tipo de material y a su vez realizar el conteo de objetos que va introduciendo el usuario. Esto último para calcular el número de puntos que se le sumarán al registro del usuario. 

Se contará con una interfaz para la interacción del usuario con el sistema la cual le facilite a cada persona introducir su id mediante RFID y clasificar correctamente cada residuo. Esto se da mediante periféricos, el movimiento de estos dentro de la maquina a realizar se hace con servomotores. Se utilizan los lenguajes de programación: Verilog, VHDL, Python y C.


Para llevar a cabo este proyecto se implementaron varios perifericos integrados de la siguiente manera:
![Bloques dig 2 (2)](https://user-images.githubusercontent.com/103794195/176984134-97b0900b-914f-47d8-8731-c13d29d31bee.png)

                
----
                    
                    
### Mapa de memoria

En este caso  el mapa de memoria nos indica la posición en memoria de cada periferico. Este se encuentra de manera detallada en el archivo Soc_MemoryMap.csv, las bases correspondientes para cada driver del SoC son las siguientes:
                    
Periferico  | Dirección Base
------------- | -------------
PWMUS  | 0X82005000
Boton | 0X82004800
Infrarrojo  | 0X82003800
Inductivo  | 0X82004000
LCD | 0X82006800
UART | 0X82006000

                
----
                    
                

### Periféricos


* LCD 

Este periferico funciona a partir de un controlador de pantalla de cristal líquido de matriz de puntos HD44780U y el controlador LSI los cuales muestran caracteres alfanuméricos y símbolos kana japoneses. En cuanto al modulo se encuentra mediante el codigo de VHDL realizando el borrado, inicialización y escritura. Mediante registros se realiza el cambio del dato a mostrar en pantalla.

Para el proyecto su funcionalidad es ser la interfaz del usuario. Es decir dar la bienvenida al usuario, mostrar en que parte del proceso se va, mostrarle al mismo el tipo de residuo que fue ingresado y los puntos obtenidos. Con respecto al flujo de datos la funcionalidad de este es de salida puesto que muestra los datos mencionados anteriormente. 

* Sensor Infrarrojo

Este sensor puede detectar objetos utilizando medios ópticos, en este caso mediante luz infrarroja. En este caso se tiene el LED de un sensor como fuente emisora y el fototransistor del otro como receptor, es decir se hace una detección de reflexión directa. Por esta razón los elementos a detectar dependen del nivel de trasparencia del material, por lo mismo solo dara une entrada correcta cuando se tenga un material con trasparencia como el plastico. 

Tiene con respecto al flujo de datos una funcionalidad de entrada de datos. Si detecta un material el dato que da este sensor pasa a ser de 1 a 0. Permitiendo así con esta variable realizar los respectivos casos para el material.


* Sensor Inductivo               

Este sensor es capaz de detectar proximidad a cierta distancia sin necesidad de hacer contacto. Esto se da gracias a la emición de una señal magnética, razón por la cual puede detectar solamente objetos ferrosos, metales y/o conductores eléctricos. Su funcionamiento se basa en la teoría del campo magnético en la que fluye una corriente inducida llamada corriente de Foucault.

Con respecto al flujo de datos la funcionalidad de este periférico es de entrada, indicando cuando el objeto a detectar es de metal. En este caso si detecta un metal el dato que da este sensor pasa a ser de 1 a 0. Permitiendo así con esta variable realizar los respectivos casos para el material.

* RFID 

![D_NQ_NP_759839-MCO40685473205_022020-O](https://user-images.githubusercontent.com/103794195/176986504-85c04533-c2a3-48bc-b6a2-8699f7493087.jpg)


El periférico de RFID o identificación por radiofrecuencia utiliza ondas de radio para enviar señales a la tarjeta y  activar la etiqueta que lleva la misma. A su vez, esta etiqueta envía una onda de regreso con información guardada en la tarjeta de forma previa. Esta tecnología RFID es una forma de comunicación inalámbrica para hacer la identificación de objetos, es decir es una tecnología que identifica el objeto a través de un lector, sin contacto y a distancia.

La funcionalidad de este lector RFID en el proyecto es la de como lo indica su nombre hacer lectura de datos, en este caso la lectura de la tarjeta va asociada a una determinada información de usuario con el ID de cada tarjeta o tag y datos asociados al mismo. Posterior a esto realiza la escritura en la base de datos con el ID de la tarjeta y el valor de los nuevos puntos del usuario.

* Servomotor

![AR0071-Servomotor-SG90-RC-9g-V1](https://user-images.githubusercontent.com/103794195/176986500-dbacf1b8-e9f7-4ef1-abd7-5c2afccb6a98.jpg)

Este periférico funciona a partir de un PWM o modulación por ancho de pulso con la cual se modula la señal que controla al servo. En este caso el servomotor a trabajar cuenta con un periodo de ancho de pulso de 20 ms, equivalente a un trabajo a 50 Hz. A su vez, este debe contar con un ciclo de trabajo de entre 1 y 2 ms dependiendo de  los grados que se desea que rote. 

Para el proyecto su funcionalidad se encuentra relacionada de forma directa con la parte mecánica del dispositivo puesto que cada servo sera el encargado de abrir la compuerta respectiva al material del residuo introducido. Con respecto al flujo de datos la funcionalidad de este periférico es de salida. Puesto que a partir de los datos de los sensores se envía la respectiva instrucción o comando al servo motor para que deje caer el residuo en el espacio correspondiente. Cada servo tendrá 2 posiciones que se les irán indicando en el proceso puesto que manejan un sistema de compuertas en el que solo se desea tener estados de abierto o cerrado.

### Construcción del prototipo

La maqueta de este prototipo se realizó en cartón piedra con diseño realizado en AutoCAD para su corte láser, se deja abierta para poder ver todo el mecanismo en funcionamiento. Los perifericos mencionados anteriormente se ubican de la siguiente manera:

* La LCD se acomodó a un costado de la maqueta para darle al usuario una buena visualización.
* Para el RFID se usó el modulo R522 el cual funciona con el protocolo de comunicación SPI, sin embargo, por facilidad de implementación en código con Litex se decidió enlazar primero a Arduino en donde se lee la etiqueta de identificación del TAG presente, analiza a que usuario corresponde en nuestro proyecto para luego enviarlo a la FPGA a través del protocolo de UART, el cual es más conocido y más comodo de utilizar. Para las pruebas de este periférico se usaron 2 TAGs correspondientes a una tarjeta y un llavero dandonos campo de acción con 2 ususarios distintos.
* En la sección en la que se pone el material a detectar se sitúan 2 sensores ópticos de infrarrojo uno frente al otro separados por el objeto a detectar en el que uno de ellos actua como transmisor todo el tiempo y no va controlado por el software, mientras que el receptor se encarga de darnos la información que detecte al momento de indicarse así en el prototipo a través del botón. Para que esto funcione correctamente se tuvo que tapar con cinta aislante el led transmisor de este modulo receptor para que la difracción presente en los materiales no afecte la medición en el proceso.
* A su vez, el sensor inductivo se situó cerca a la compuerta donde se deposita el material ya que su rango de alcance de detección es realmente corto.
* Para la sección de separación de los depósitos según el material se usaron 3 servomotores con una lógica basada en una rampa y varias compuertas. El primer servomotor se sitúa justo debajo de la bandeja en la que se realiza la detección del material y es el último en accionarse ya que primero debe ser activado el motor correspondiente al material sensado para que al dejarlo caer ya tenga la ruta correspondiente que debe seguir para llegar a su respectiva caneca. Este control de separación se realizó por medio de una rampa, en la que al tratarse de 3 depósitos distintos se usaron solo 2 servomotores con 2 compuertas, dejando el último depósito abierto todo el tiempo.

Por otra parte, en cuanto a conexiones con la FPGA y la alimentación se usaron voltajes de 3.3V y 5 V correspondientes al de la FPGA y el arduino respectivamente, los módulos que trabajan con 5 V y se leían como señal de entrada en la FPGA pasaron primero por un acondicionamiento de señal con un conversor de niveles de 5 V a 3.3 V ya que es el voltaje máximo soportado por los PMODS de la FPGA. Como caso especial para los servomotores alimentados por 5 V, controlados por señales de salida de la FPGA, se enlazaron primero a un optoacoplador a modo de protección de la FPGA puesto que estos en un mal funcionamiento, obstrucción de su movimiento o modificación manual de este puede devolver una corriente hacia esta y quemar los PMODS conectados.

![WhatsApp Image 2022-07-01 at 11 00 38 PM (1)](https://user-images.githubusercontent.com/103794195/176986524-b513bc61-34ec-4a98-965b-5be084717050.jpeg)

![WhatsApp Image 2022-07-01 at 11 00 38 PM](https://user-images.githubusercontent.com/103794195/176986536-93ec6eed-8466-4991-b219-5af496886ea7.jpeg)

![WhatsApp Image 2022-07-01 at 11 01 17 PM](https://user-images.githubusercontent.com/103794195/176986540-cbf934c7-3f4d-408f-a7f3-5151518e8e4b.jpeg)

![WhatsApp Image 2022-07-01 at 11 02 09 PM](https://user-images.githubusercontent.com/103794195/176986544-66d91bbc-ecc6-4c09-ad04-b666e011ffc7.jpeg)

