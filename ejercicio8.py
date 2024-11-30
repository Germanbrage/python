"""
EJERCICIO 8: FUNCION encontrar_puesto_empleado
Crea una función que tome un nombre completo y una lista de empleados, 
busque el nombre completo en la lista y devuelve el puesto del empleado si 
está en la lista, de lo contrario, devuelve un mensaje indicando que la persona 
no trabaja aquí.
"""

def encontrar_puesto_empleado(nombre):
  empleados= [{'nombre':"Juan",'apellido':"García",'puesto':"product manager"},
              {'nombre':"Clara",'apellido':"Carrasco",'puesto':"community manager"},
              {'nombre':"Pepe",'apellido':"Pantin",'puesto':"CEO"}]
  for empleado in empleados:
     if empleado['nombre'] == nombre:
       return empleado['puesto']
  raise ValueError(f"{nombre} no trabaja en esta empresa")

try:
  print (f"encontrar_puesto_empleado(Juan)=",encontrar_puesto_empleado("Juan"))
except ValueError as e:
  print (f"error:{e}")
try:
  print (f"encontrar_puesto_empleado(María)=",encontrar_puesto_empleado("María"))
except ValueError as e:
  print (f"error:{e}")