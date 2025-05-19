#practica de polimorfismo
class Animal:
    def __init__(self, nombre,raza):
        self.nombre = nombre
        self.raza= raza
    
    def hacer_sonido(self):
        return "Sonido genérico"

class Perro(Animal):  # Perro hereda de Animal
    def hacer_sonido(self):
        return "Guau guau"
    
def hacer_sonar(animal):
    print(animal.hacer_sonido())

gato = Animal("Tilin")
perro = Perro("Balu")

hacer_sonar(gato)  # Llama al método de Animal
hacer_sonar(perro)  # Llama al método sobreescrito en Perro
