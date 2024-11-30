"""
EJERCICIO 10: FUNCION resto_division
Crea una función lambda que calcule el resto de la división entre dos números dados
"""
restolambda = lambda x, y: x % y
x=10 
y=3
if y !=0:
  print (f"El resto de dividir {x} entre {y} es:",restolambda(10,3))
else:
  print ("Error: el divisor no puede ser cero")