import requests 
import json

class GestorJson :
    def __init__(self, arch):
        self.arch = arch 
    def leerJson(self):
        try:
            with open(self.arch, 'r') as f:
                 return json.load(f)
        except FileExistsError:
            print("Archivo no existe")
        except json.JSONDecodeError:
            print('El archivo no es Json')
            return{}
    def escribirJson(self, datos):
            with open (self.arch, 'w') as f:
                 return json.dump(datos, f , indent=4)
    def modificarJson (self, llave, valor ):
         datos = self.leerJson()
         datos[llave] = valor
         self.escribirJson(datos)
    def obtenerPoke(self, pokemon):
        try:
            Url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
            response = requests.get(Url)
            response.raise_for_status()
            data = response.json()
            self.escribirJson(data)
            print("KLk")
        except requests.exceptions.HTTPError:
             print('El enlace no existe')
        except requests.exceptions.RequestException:
             print('No se pudo realizar la peticion')
             

gjson = GestorJson("pokemon.Json")
gjson.obtenerPoke("Pikachu")
pokeinfo = gjson.leerJson()
p = pokeinfo["abilities"]
print(p)