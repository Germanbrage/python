"""
EJERCICIO 3.:FUNCION encontrar_duplicado
Crea una función que busque y devuelva el primer elemento duplicado en una 
lista dada.
"""

list = [1,3,6,5,3,7,7]
def encontrar_primer_duplicado (list):
  numeros_duplicados = set()
  for numero in list: 
    if numero in numeros_duplicados:
      return numero
    numeros_duplicados.add(numero)
  return None
print (f"encontrar_primer_duplicado {list} : {encontrar_primer_duplicado (list)}")