#Fermin Martinez Velazquez
class Persona:
    def __init__(self, nombre, edad):#inicializa doblem método, esta inicializando los atribytos y métodos, eso es un constructor. init toma en cuenta que se puede acceder directamente o que es privado 
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad  # Atributo privado
    
    def get_nombre(self):  # Método público para acceder a __nombre
        return self.__nombre
    
    def set_edad(self, nueva_edad):  # Método público para modificar __edad
        if nueva_edad > 0:
            self.__edad = nueva_edad
# 1. Encapsulamiento: Restringe el acceso a los atributos de un objeto. y permite su modificación solo a través de métodos controlados.
#expone solo lo necesario a través de métodos públicos
