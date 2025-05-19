#11-02-2025
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
