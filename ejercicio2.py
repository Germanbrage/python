list = [1,2,3,4,5,6]
def calcular_promedio (list):
  valor = 0 
  contador = 0
  for _ in list: 
   valor += _
   contador += 1
  return valor/contador
print (f"calcular_promedio {list} : {calcular_promedio (list)}")