#07-04-2025
#Diseño de interfaces de usuario: ISO 9241-210 y Heuristicas
#Psicologia del diseño y modelos mentales           
#Paquete para python: Flask y streamlit (se trabaja con html5, css y js)
#Frameworks: Django (Este es otra manera de hacer
#------------------------------------------------------------------------
#Diseño de interface
"""
Jerarquia / Organizacion de elemntos
familiaridad y concistencia
Design thinking
principios de UX
Usabilidad y Accesibilidad
Live Server(Ext VSC)

threejs maneja objetos en tercera dimencion
canvas
videos
audio
instalar extencion de Live server y visitar threejs
traer un video, un audio, imagen
"""
from flask import Flask #Traer un paquete 

app = Flask(__name__) #se inicializa el objeto flask

@app.route('/') #parametro de la ruta a la que queremos acceder, cada que se acceda al decorador se ejecura la funcion
def hola_mundo(): #Cada que la ruta sea hola se manda a imprimir el hola mundo  
    return "Hola mundo"

if __name__  == "__main__": #Si name es igual a main se imprime la pagina
    app.run(debug=True)# se corre la aplicacion completa

