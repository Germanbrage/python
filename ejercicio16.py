"""
EJERCICIO 16: FUNCION procesar_texto:
 Crea una función llamada procesar_texto que procesa un texto según la opción especificada: 
contar_palabras , reemplazar_palabras , eliminar_palabra . Estas opciones son otras 
funciones que tenemos que definir primero y llamar dentro de la función procesar_texto .
"""

def contar_palabras(texto):
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        palabra = palabra.lower().strip(",.?!")
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra_a_eliminar):
    palabras = texto.split()
    palabras_filtradas = [palabra for palabra in palabras if palabra != palabra_a_eliminar]
    return ' '.join(palabras_filtradas)

def procesar_texto(texto, opcion, *args):
    if opcion == "contar_palabras":
        return contar_palabras(texto)
    elif opcion == "reemplazar_palabras":
        if len(args) != 2:
            raise ValueError("Se necesitan dos argumentos: palabra_vieja y palabra_nueva.")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar_palabra":
        if len(args) != 1:
            raise ValueError("Se necesita un argumento: palabra_a_eliminar.")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida. Usa 'contar_palabras', 'reemplazar_palabras' o 'eliminar_palabra'.")


texto = "Este es un ejemplo de texto. Este texto contiene palabras repetidas."
frecuencia = procesar_texto(texto, "contar_palabras")
for palabra, cantidad in frecuencia.items():
    print(f"'{palabra}': {cantidad} veces")
print(procesar_texto(texto, "reemplazar_palabras", "texto", "relato"))
print(procesar_texto(texto, "eliminar_palabra", "ejemplo"))