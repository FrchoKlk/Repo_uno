#6-02-2025
from numpy import array 
import numpy as np

class Arreglos:
    def __init__(self, v):
        self.arregloMP = np.array(v)
        self.arreglosList = [v]
    
    def insertar(self, v):
        self.arreglosList.append(v)
    
    def insertarMP(self, v, i):
        self.arregloMP = np.insert(self.arregloMP, i, v)
    
    def eliminar(self, i):
        self.arreglosList.pop(i)
    
    def eliminarMP(self, i):
        self.arregloMP.delete(i)
    
    def modificar(self, i, v):
        self.arreglosList[i] = v

    def modificarMP(self, i, v): 
        self.arregloMP [i] = v



