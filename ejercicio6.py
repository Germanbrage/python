"""
EJERCICIO 6: FUNCION buscar_nombre
Crea una función que solicite al usuario ingresar una lista de nombres y luego 
solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se 
imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza 
una excepción.
Incorpora los siguientes nombres a la lista y comprueba que la función 
funciona correctamente: "Jaime", "Silvia" y "Ana".
"""

def buscar_nombre(nombre):
  list = ["Jaime","Silvia","Ana"]
  if nombre not in list:
    raise ValueError("El nombre no se encuentra en la lista.")
  return f"{nombre} está en la lista"

try: 
  print (f"buscar_nombre ({"Ana"}):{buscar_nombre("Ana")}")
except ValueError as e:
  print (f"error:{e}")