"""Desarrollar un programa que conste de una clase padre Cuenta y dos subclases PlazoFijo y CajaAhorro. 
Definir los atributos titular y cantidad y un método para imprimir los datos en la clase Cuenta. 
La clase CajaAhorro tendrá un método para heredar los datos y uno para mostrar la información.
La clase PlazoFijo tendrá dos atributos propios, plazo e interés. 
Tendrá un método para obtener el importe del interés (cantidad*interés/100) y otro método para mostrar la información, datos del titular plazo, interés y total de interés."""

class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
    
    def mostrar_informacion(self):
        return f'Titular: {self.titular}\nCantidad: {self.cantidad}'
    

class CajaAhorro(Cuenta):
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)

class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes
    
    def obtener_interes(self):
        if not isinstance(self, PlazoFijo):
            print('La cuenta no un Plazo Fijo')
            return
        interes = self.cantidad * self.interes / 100
        return interes
    
    def mostrar_informacion(self):
        print(f'Titular: {self.titular}')
        print(f'Plazo: {self.plazo}')
        print(f'Interés: {self.interes}')
        print(f'Total de Interés: {self.obtener_interes()}')

#Instancia de una cuenta
cuenta1 = Cuenta('Matilda', 2000)
caja_ahorro1 = Cuenta('Juan Perez', 1000)
plazo_fijo1 = PlazoFijo('Mauricio Macri', 5000, 30, 8)

# Mostrar informacion de la cuenta
print(cuenta1.mostrar_informacion())
print(caja_ahorro1.mostrar_informacion())
print(cuenta1.obtener_interes())




