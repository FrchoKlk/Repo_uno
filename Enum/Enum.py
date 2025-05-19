#Enum: maneja secuencias, tiene la capacidad de asignar un valor numerico 
#Ejemplo:
"""
lunes = 1 
martes = 2
miercoles = 3 
jueves = 4
viernes = 5
"""
from enum import Enum 
class consecutivo (Enum):
    #Esos valores tienen un nombre representativo 
    lunes = 1
    martes = 2
    miercoles = 3
print(consecutivo.lunes)
print(consecutivo.lunes.value)
print(type(consecutivo.lunes))
print(type(consecutivo.lunes.value))
#Se instansea la clase sin nesecidad de crear un objeto  

from typing import Final 
class Usuario:
    max__inventario : Final = 1000

try:
    V = 5/0      #<----ZeroDivicionError
except: #Aqui va el nombre del error 
    "no sirve"
finally:
    print("error desconocido")