"""
EJERCICIO 13: FUNCION sumar_listas
Crea una función lambda que sume elementos correspondientes de dos listas dadas.
"""

lista1 = [1,1,1]
lista2 = [2,2,2]
sumar_listas = map(lambda x,y:x+y,lista1,lista2) 
print (f"sumar_listas:",list(sumar_listas))
