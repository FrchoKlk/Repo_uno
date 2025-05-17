import time
import threading 
class hilo (threading):
    def __init__(self, nombre, intervalo):
        super().__init__()
        self.nombre = nombre
        self.intervalo = intervalo 
    def run (self):
        print(f"El hilo {self.nombre} a comenzando")
        for i in range (5):
            print(f"El hilo {self.nombre} esta en la iteracion {i}")
            time.sleep(self.intervalo)
        print(f"El hilo {self.nombre} a finalizado")

Hilo1 = hilo("hilo1", 2)
Hilo2 = hilo("hilo2", 4)
