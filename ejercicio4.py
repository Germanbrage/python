"""
EJERCICIO 4: FUNCION enmascarado_datos
Crea una función que convierta una variable en una cadena de texto y 
enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.
"""

def enmascarado_datos(variable):
   variable_str = str (variable)
   if len(variable) <= 4 :
     return variable_str
   else:
     return '#' * (len(variable_str)-4) + variable_str[-4:] 
print (f"enmascarado_datos : {enmascarado_datos ('32720107P')}")