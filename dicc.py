#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

Script que abre el fichero /etc/passwd, toma todas sus líneas
en una lista y las guarde en un diccionario

Imprime por pantalla los valores para el usuario 'root' y para
el usuario 'imaginario'. El segundo produce un error; evitar el 
error mediante excepciones.

"""

# Abre el fichero en modo lectura
fich = open("/etc/passwd","r")
# Leemos todas las líneas del archivo
lineas = fich.readlines()
# Diccionario
dicc = {}

# Que recorra todas las líneas y que me escoja la que yo quiero

for linea in lineas:
        # Dividimos en trozos a partir del carácter delimitador ':' y
        # cogemos el trozo que nos interesa. Para el caso del login es 
        # la posición 0 y para la shell podemos poner [6] o [-1]; con 
        # [-1] sería como el anterior al primero, que es la última posición,
        # y con [6] porque la shell está en la posición 6 de nuestra lista.
        login = linea.split(':')[0]
        shell = linea.split(':')[6][:-1]
        # Key 
        dicc[login] = shell

print("Los valores para el usuario root: ", dicc['root'])

try:
    usu = dicc['imaginario']
except KeyError:
    print("Ese usuario no existe.")


    

    

    
