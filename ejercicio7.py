"""
EJERCICIO 7: FUNCION fibonacci
Crea una función que calcule el término n de la serie de Fibonacci utilizando 
recursión.
La secuencia de Fibonacci es una serie de números en la que cada número es 
la suma de los dos números anteriores, comenzando con 0 y 1. La posición 0 
es la primera.
"""

def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
  
print ("fibonacci (4)=", fibonacci (4))
