#11-02-2025
#Ejemplo de Abstraccion
from abc import ABC, abstractmethod #abc sirve para importar clases abstractas
class Auto(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca 
        self.modelo = modelo                                                    
    
    abstractmethod
    def arrancar(self):
        pass #Es un manera de pasar de linea, para que haga lo que quiera 
    abstractmethod
    def frenar (self):
        pass

class Deportivo(Auto):
    def arrancar(self):
        return f"{self.marca}{self.modelo} arrancar con un rujido deportivo "
    def frenar (self):
        return f"El {self.marca} {self.modelo} frena rapidamente"
Mi_auto = Deportivo ("Ferrari", "Marella")
print(Mi_auto.arrancar())
print(Mi_auto.frenar())

#Ejemplo de Ecapsulamineto 
class persona:
    def __init__(self, nombre, edad): #La Funcion de los guiones bajos, el constructuor inicializa tomando en cuanta que es publico y que es privado
        self.nombre = nombre 
        self.__edad = edad # type: ignore # no se puede acceder de forma directa y sirve para ahorrar memoria
    def mostrarEdad(self):
        return self.__edad

p  = persona("Ana", 25)
print (f"nombre: {p.nombre}")
print (f"Edad: {p.mostrarEdad}")
    
#Ejemplo de herencia 
class animal:
    def __init__(self, nombre):
        self.nombre = nombre 
    def hacerSonido(self):
        return "Sonido generico"
class perro(animal):
    def hacerSonido(self):
        return "guau guau"
    #objetos genericos
perrito = perro ("firulais")
print(perrito.nombre)
print(perrito.hacerSonido())

#Segundo ejemplo de herencia

class vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca 
        self.modelo = modelo
#Para que se utiliza encapsulamineto? Si se quieren dan dar atributos privados o atributos publicos
#Herencia: Se heredan atributos, funciones, metodos, heredados del padre
#Poliformismo: funciona diferente depende de la clase que lo este llamando 
#Abstrancia: Utilizas 

#Ejemplo de abstraccion
#pisteasa
class pisto:
    def __init__(self, hieliera, hielera2):
        self.__hieliera = hieliera
        self.hieliera2 = hielera2
    def pistear (self):
        self.__hieliera = "vaciar"
        return self.__hieliera
    def pistear2 (self):
        self.hieliera2 = "Mah, esta vacia"
        return self.hieliera2

fiesta = pisto ("Carton en hielera", " Unas cuantas frias")
print(fiesta.pistear())
print(fiesta.pistear.hielera2) 