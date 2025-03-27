#30-01-2025
#Fermin Martinez Velazquez
import math 
class figura():
    def Area (Caras, largo):
        if Caras == 3:
            b = largo / 2 
            a = largo 
            c = math.sqrt(a**2-b**2)
            are = (largo * c) / 2
            print("El area del trinagulo es: ", are)
        elif Caras == 4:
            are = Caras * Caras
        elif Caras == 5:
            p = largo * 5 
            a = largo / 1.45 
            are = (p * a) / 2
    def Perimetro(caras, largo):
        if caras == 3:
            peri = largo * caras 
            print("El perimetro del triangulo: ", peri)
        elif caras == 4:
            peri = largo * caras
            print("El perimetroo del cuadrado es: ", peri)
        elif caras == 5:
            peri = largo * caras
            print("El perimetro de el pentagono es: ", peri)

A = figura.Area(3,4)
P = figura.Perimetro(3,5)