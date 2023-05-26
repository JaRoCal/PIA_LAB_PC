## PRACTICA11_1970947

### en esta práctica de escáner de puertos se realizaron varios ejercicios enfocados en el desarrollo de pequeñas piezas de software desarrolladas en Python para el escaneo de puertos.
___
### SCAN_PORTV1 
Se construyó el script scan_portv1.py con las siguientes partes:

Parte1: Se importan las librerías requeridas:
~~~
#!/usr/bin/python
# -*- coding: utf-8 -*-
#Parte 1 
#Importamos librerias necesarias
import sys
from socket import *
~~~
Parte2: Se piden como argumentos del script la dirección ip y el rango de puertos a escanear 
~~~
#Parte 2
#Modo de ejecucion del script
# port_scan.py <host> <start_port>-<end_post>
#Primer argumento se guarda en variable host
#Segundo argumento de guarda en portstrs
host = sys.argv[1]
portstrs = sys.argv[2].split('-')
~~~
Parte3: El rango de puertos proporcionado como segundo argumento se transforma en una 
lista de la que se obtienen dos valores: 
~~~
#Parte 3
#portstrs contiene dos valores que asignamos
#en start_port e valor de inicio
#en end_port el valor fin 
start_port = int(portstrs[0])
end_port = int(portstrs[1])
~~~
Parte4: El argumento originalmente guardado como host se procesa con la función 
gethostbyname para obtener una dirección ip; también se crea una lista para almacenar los 
puertos que se encontraron abiertos:
~~~
#Parte 4 
#Para usar en el socket sasignados lo de la
#variable host a target_ip
#Definimos una lista de puertos opened_ports
target_ip = gethostbyname(host)
opened_ports = []
~~~
Parte5.- Iniciamos un bucle for para con sockets ir probando los puertos obtenidos del rango de 
puertos, si el resultado es 0 se agregan a la lista de opened_ports:
~~~
#Parte 5 
#Iniciamos bucle for para probar los puertos 
for port in range (start_port, end_port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        opened_ports.append(port)
~~~
Part6: Se imprimen los resultados:
~~~
#Parte 6 
#Se imprime salida 
print("Opened ports:")
#
for i in opened_ports:
    print(i)
~~~
### SCAN_PORTV2 
A continuación, se construyó el script scan_portv2.py en base a las siguientes partes: 
1.-Parte1: Se importan las librerías requeridas:
~~~
#Parte 1 
#Importamos librerias requeridas
import socket
~~~
Parte2: Se define la función scan sobre la que usando sockets se estarán probando los 
diferentes puertos:
~~~
#Parte 2 
#Se define la funcion scan con la cual
#se utilizan sockets para probar los diferentes 
#puertos
def scan(addr, port):
    #Creando un nuevo socket 
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Estableciendo el timeout para el nuevo objeto tipo socket
    socket.setdefaulttimeout(1)

    #Conexion exitosa devuelve 0. Devuelve error en caso contrario
    result = socket_obj.connect_ex((addr,port)) #Direccion y puerto en tupla.

    #Se cierra el objeto
    socket_obj.close()

    return result
~~~
Parte3: Se establece una lista de puertos, que para fines prácticos se recomienda sea un 
número limitado
~~~

~~~
