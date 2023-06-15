class Cuenta:
    def __init__(self, titular, cantidad = 0):
        self.titular = titular
        self.cantidad = cantidad
    
    def mostrar(self):
        print(f'Titular: {self.titular}\nCantidad: {self.cantidad}')

    def ingresar(self, cantidad_ingreso):
        if cantidad_ingreso > 0:
            self.cantidad += cantidad_ingreso
    
    def retirar(self, cantidad_retiro):
        if cantidad_retiro > 0:
            self.cantidad -= cantidad_retiro

# Instanciar objeto
cuenta1 = Cuenta('Antonela Ruelli', 10000)

# Mostrar
cuenta1.mostrar()

# Ingresar dinero
cuenta1.ingresar(5000)
cuenta1.mostrar()

# Retirar dinero
cuenta1.retirar(50000)
cuenta1.mostrar()