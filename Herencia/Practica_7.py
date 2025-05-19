#Practica de Herencia
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
