"""
EJERCICIO 14: No te vayas por las ramas 
Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los 
métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . 
El objetivo es implementar estos métodos para manipular la estructura del árbol.
"""

class Rama:
    def __init__(self, id_rama, longitud=1):
        self.id_rama = id_rama
        self.longitud = longitud

    def crecer(self):
        self.longitud += 1


class Arbol:
    def __init__(self,):
        self.longitud_tronco = 1
        self.ramas = []
        self.siguiente_id_rama = 1

    def crecer_tronco(self):
        self.longitud_tronco += 1

    def nueva_rama(self):
        nueva_rama = Rama(self.siguiente_id_rama)
        self.ramas.append(nueva_rama)
        self.siguiente_id_rama += 1

    def crecer_ramas(self):
        for rama in self.ramas:
            rama.crecer()

    def quitar_rama(self, id_rama):
        self.ramas = [rama for rama in self.ramas if rama.id_rama != id_rama]

    def info_arbol(self):
        return {
            "longitud_tronco": self.longitud_tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": {rama.id_rama: rama.longitud for rama in self.ramas}
        }


# Crear un árbol
Abeto = Arbol()

# Hacer crecer el tronco del árbol una unidad
Abeto.crecer_tronco()

# Añadir una nueva rama al árbol
Abeto.nueva_rama()

# Hacer crecer todas las ramas del árbol una unidad
Abeto.crecer_ramas()

# Añadir dos nuevas ramas al árbol
Abeto.nueva_rama()
Abeto.nueva_rama()

# Retirar la rama situada en la posición 2
Abeto.quitar_rama(2)

# Obtener información sobre el árbol
info = Abeto.info_arbol()
print(info)
