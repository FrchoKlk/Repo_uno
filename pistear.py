#Ejemplo de encapsulaminto
#12-02-2025
class pisto:
    def __init__(self, hieliera, hielera2):
        self.__hieliera = hieliera
        self.hieliera2 = hielera2
    def pistear (self):
        self.__hieliera = "vaciar"
        return self.__hieliera
    def pistear2(self):
        self.hieliera2 = "Mah, esta vacia"
        return self.hieliera2

fiesta = pisto ("Carton en hielera", " Unas cuantas frias")
print(fiesta.pistear())
print(fiesta.pistear2()) 
