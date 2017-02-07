# 13.5 Diccionario
fich = open("/etc/passwd","r")
# LISTA DE LINEAS
lineas = fich.readlines()
dicc = {}

for linea in lineas:
        login = linea.split(':')[0]
        shell = linea.split(':')[-1][:-1]
        print(login, shell)

print"La shell de root:, dicc["root"]

try:
    print(dicc["imaginario"])
except:
    print("imaginario no existe.")
    
    
