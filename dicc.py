#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

Script que abre el fichero /etc/passwd, toma todas sus líneas
en una lista e imprime, para cada identificador de usuario, la
shell que utiliza

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

print("La shell de root:", dicc["root"])

try:
    print(dicc["imaginario"])
except KeyError:
    print("imaginario no existe.")
    
    
