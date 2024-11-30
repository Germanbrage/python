"""
EJERCICIO 15: CLASE usuario banco
Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si 
tiene o no cuenta corriente. Proporciona métodos para realizar operaciones 
como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
"""

class UsuarioBanco:
    siguiente_id_usuario = 1

    def __init__(self, nombre, saldo_inicial=0, tiene_cuenta_corriente=False):
        self.id_usuario = UsuarioBanco.siguiente_id_usuario
        UsuarioBanco.siguiente_id_usuario += 1
        self.nombre = nombre
        self.cuentas = []
        if tiene_cuenta_corriente:
            self.agregar_cuenta(saldo_inicial)

    def agregar_cuenta(self, saldo_inicial=0):
        nueva_cuenta = CuentaCorriente(saldo_inicial)
        self.cuentas.append(nueva_cuenta)
        return nueva_cuenta


class CuentaCorriente:
    siguiente_id_cuenta = 1

    def __init__(self, saldo_inicial=0):
        self.id_cuenta = CuentaCorriente.siguiente_id_cuenta
        CuentaCorriente.siguiente_id_cuenta += 1
        self.saldo = saldo_inicial

    def ingresar_saldo(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return True
        return False

    def retirar_saldo(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False

    def transferir(self, cantidad, cuenta_destino):
        if self.retirar_saldo(cantidad):
            cuenta_destino.ingresar_saldo(cantidad)
            return True
        return False

# Crear usuarios con cuenta corriente
usuario1 = UsuarioBanco("Alicia", saldo_inicial=100, tiene_cuenta_corriente=True)
usuario2 = UsuarioBanco("Bob", saldo_inicial=50, tiene_cuenta_corriente=True)

# Mostrar saldos iniciales
print(f"Saldo inicial de {usuario1.nombre}: {usuario1.cuentas[0].saldo}")
print(f"Saldo inicial de {usuario2.nombre}: {usuario2.cuentas[0].saldo}")

# Agregar 20 unidades de saldo a "Alicia"
usuario1.cuentas[0].ingresar_saldo(20)
print(f"Saldo después de agregar 20 unidades a {usuario1.nombre}: {usuario1.cuentas[0].saldo}")

# Hacer una transferencia de 80 unidades desde "Bob" a "Alicia"
if usuario2.cuentas[0].transferir(80, usuario1.cuentas[0]):
    print(f"Transferencia de 80 unidades de {usuario2.nombre} a {usuario1.nombre} realizada con éxito.")
else:
    print(f"Transferencia de 80 unidades de {usuario2.nombre} a {usuario1.nombre} fallida por saldo insuficiente.")

# Mostrar saldos después de la transferencia
print(f"Saldo de {usuario1.nombre} después de la transferencia: {usuario1.cuentas[0].saldo}")
print(f"Saldo de {usuario2.nombre} después de la transferencia: {usuario2.cuentas[0].saldo}")

# Retirar 50 unidades de saldo a "Alicia"
if usuario1.cuentas[0].retirar_saldo(50):
    print(f"Retiro de 50 unidades de {usuario1.nombre} realizado con éxito.")
else:
    print(f"Retiro de 50 unidades de {usuario1.nombre} fallido por saldo insuficiente.")

# Mostrar saldo final de "Alicia"
print(f"Saldo final de {usuario1.nombre}: {usuario1.cuentas[0].saldo}")

