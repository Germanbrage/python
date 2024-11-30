"""
EJERCICIO 12: FUNCION numeros_suma usando lambdas y map 
Crea una función lambda que sume 3 a cada número de una lista dada. 
"""
numeros = [24,56,2.3,19,-1,0]
numeros_suma = map (lambda x:x+3,numeros)
print (f"numeros_suma {numeros}:",list(numeros_suma)) 
