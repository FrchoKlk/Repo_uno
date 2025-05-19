#13-02-2025
from enum import Enum

class Dias(Enum):
    Lunes = "Lunes"
    Martes = "Martes"
    Miercoles = "Miercoles"
    Jueves = "Jueves"
    Viernes = "Viernes"
    Sabado = "Sabado"
    #No se utiliza self porque se tiene Enum
    def verificar_dia(dia):
        try:
            if not isinstance(dia, str): #aqui se realiza una comparacion 
                raise TypeError ("Se esperaba un valor del tipo string") #Se lanza esste mensaje si no se da un valor string 
            dia = dia.capitalize()

            if dia in [d.value for d in Dias]:
                print(f"Dia valido: {dia}")
            else:
                raise ValueError("El dia ingresado no es valido, debe ser un dia de la semana")
            
        except TypeError as e:
            print(f"Error de tipo: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            print("Ejecucion finalizada")

        
v = Dias.verificar_dia("Lunes")
p = Dias.verificar_dia("Feriado")
o = Dias.verificar_dia(123)
       

    