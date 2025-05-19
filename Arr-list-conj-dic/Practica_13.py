#01-04-2025
c = {0, 1, 2, 3, 4, 5}
c.add (6)
c.remove(4)
c.discard(7)
c.add(3)

print( 3 in c)

#Conjudntos
A = {1, 2, 3}
B = {3, 4, 5}
U = B.union(A) # | es igual que el union
I = B.intersection(A) # El & es igual que el interssection
D = A.difference(B) # El - es igual que difference 
C = A.symmetric_difference(B) # Para la diferencia simetrica es ^ 
print(C)
print(D)
print(U)
print(I)
 
N = {1, 2, 3}
M = {1, 2, 3}
N.issubset(M)
M.issuperset(N)
V = len(A) # contar elementos dentro de un conjunto 
print(V)
N.clear() # Limpia los conjuntos 
E = N.copy()
A.isdisjoint(B) # verifica si hay elementos conpartidos 

#Diccionarios
Dck = {"x" : "equis", "y" : "ye", "d" : "de"}
Dck2 = dict (x = "equis", y = "ye", d="de") # Manera de declarar tambien un diccionario 
print(Dck['x'])
print(Dck2.get['x'])
print(Dck.get('z'))
Dck['x'] ="equisd" 
Dck2 ['z'] = "zeta"# agrega elimentos al ddiccionariio 
del Dck ['y'] # se utiliza para eliminar elemento dentro del diccionario  
x = Dck.pop ('y')
print (x)
print ('x' in Dck)
llaves = Dck.keys()#podemos tener todas las variables 
print(llaves) # Lo muestra como lista 
valores = Dck.values()
P = Dck.items() # Lo convierte a tuplas 
# regresa ([(y), (x)])
Dck.clear
Dck.update({x : "ekis"})
Dck.get("x", "equis") #Aqui solamente cuando el valor es igual
