"""
EJERCICIO 11: FUNCION numeros_pares
Crea una función lambda que filtre los números pares de una lista dada.
"""

def numeros_pares(numero):
  return numero % 2 == 0
numeros = [1,2,3,4,5,6,7,8,9]
pares = filter(numeros_pares,numeros)

print (f"numeros_pares {numeros}:",list(pares))

pareslambda = filter (lambda x: x% 2 ==0,numeros)
print (f"pareslambda:",list(pareslambda))
