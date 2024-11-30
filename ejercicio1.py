"""
EJERCICIO 1: FUNCION contar_carácteres
Crea una función que cuente el número de caracteres en una cadena de texto 
dada.
"""

def contar_caracteres (palabra):
   caracteres = 0
   for _ in palabra: 
     caracteres += 1
   return caracteres
palabra = "caballo"
print (f"contar_caracteres ({palabra})= {contar_caracteres(palabra)}")
