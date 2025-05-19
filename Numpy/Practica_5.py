#27-03-2025
import numpy as np
#np.array() # nadamas permite un solo tipo de dato, si se introduce cadena todo los demas seran cadenas

arreglo = []
arreglo = list () # tambiens asi se declaran arreglos 

tupla = ()
tupla = tuple() # la tupla es inmutable, una vez que se crea ocupa un espacio en memoria y no se modifican los datos

x = 1, 2, 3, 1
x = set() # palabra para crear conjuntos, los elementos repetidos se eliminan 
x.intersection#(y)
x = {} # Asi se puede inicializar un conjunto, pero si esta vacio es un diccionario 

x = dict() # Asi se declara un diccionario
x = {"llave":"valor"} # tambien asi se declara un diccionario y tiene que llevar llave y valor 
# En el diccionario para buscar un elemenato, se llama mapeo y para hacer essto se necesita proporcionar la llave del elemento
# Los dicionarios por su estrucruta pueden ser comvertidos a json porque comparten la misma esstructura 
# Para guardar se necesita una paquete llamado pandas 

list = ["R", 3, 3.4, True, 5]
lista2 = np.array ([1, 2, 5])
tupla = tuple(list)
tupla2 = tuple(lista2)
conj = set(list)
conj2 = set(lista2)
D = dict["llave" : 4, "llave2" : 2.0, "llave3" : True, "llave3" : "valor", "llave4" : {1}]
print()

list.append(5) # Con el comando append se agrega un elemento
list.insert(4, "hola") #Se da la posicion donde tiene quiere que vaya el valor
list.extend([2, "hola2"]) #se pueden agragar mas de 2 elementos y se agragan al final 
list.index(1) # Este comando dice la posicion del elemento que se busca
list.count(1) # Este comando busca y cuenta el elemento que se busca 
x = 1 in  list #Buscar en chat gepete

#1-04-2025 
# buffer se deben establecer protocolos 
# Raw Entra en las 3 primeras capas del modelo osi, se hacen todas las conexiones necesarias para presenrtar la inforamcion
#Metodo F\S para poder manejar archivos 
#Abrir opend()       Escribir write()
#cerrar close()      Leer read ()

#Esas funciones las maneja pandas 
# Los txt se pueden convertir a un numero binario, y en la mayoria de  los archivos son binarios
# kali linux hacking etico 
# La diferencia de un diccionario y un json 
#json: se almacena en un archivo txt, no importa si todos los elementos estan en el mismo nivel  
#dict: se almacena en la memoria, 
# Atraves de pickle, investigar que pdo 
# comando seek("x") se utiliza para posicionar 
# teld() te dice en que posicion se encuentra el cursos 
# flush() Elimina datos y lo deja vacion, trabaja con el buffer 
#truncate () redimenscionar, resize 