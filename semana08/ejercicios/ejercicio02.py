# Definición de clases
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'El vehículo es de color {self.color} y tiene {self.ruedas} ruedas'

    def mostrar_tipo(self):
        return self.__class__.__name__
    
    def mostrar_ruedas(self):
        return self.ruedas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return f'{super().__str__()} con vel. max de {self.velocidad} km/h y {self.cilindrada} L de cilindrada'

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return f'{super().__str__()} y carga {self.carga} kg'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'{super().__str__()} es de tipo {self.tipo}'

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return f'{super().__str__()} con una vel. max de {self.velocidad} km/h y {self.cilindrada} cm3 de cilindrada'

def catalogar(lista):
    for elemento in lista:
        objeto = vars(elemento) # Cada objeto genera un diccionario de atributos y datos
        for atributo, valor in objeto.items(): # Cada par de (atributo, valor) son una tupla
            print(f'Atributo: {atributo} --> {valor}')
        print('='*30)

def catalogar_con_ruedas(lista, ruedas = 0):
    contador = 0
    for elemento in lista:
        if elemento.mostrar_ruedas() == ruedas:
            contador += 1
            objeto = vars(elemento) 
            for atributo, valor in objeto.items():
                print(f'Atributo: {atributo} --> {valor}')
            print('='*30)
    print(f'Se han encontrado {contador} vehículos con {ruedas} ruedas')



# Instancias    
fitito = Vehiculo('Celeste', 4)
auto1 = Coche('Verde', 4, 180, 1.6)
chata1 = Camioneta('Marrón', 4, 220, 2.8, 1000)
bici1 = Bicicleta('Azul', 2, 'deportiva')
moto1 = Motocicleta('Gris', 2, 'urbana', 100, 110)

# Ejecuciones
"""print(fitito)
print(fitito.mostrar_tipo())
print(auto1)
print(auto1.mostrar_tipo())
print(chata1)
print(chata1.mostrar_tipo())
print(bici1)
print(bici1.mostrar_tipo())
print(moto1)
print(moto1.mostrar_tipo())
"""
lista_vehiculos = (fitito, auto1, chata1, bici1, moto1)
#print(lista_vehiculos)

#catalogar(lista_vehiculos)
catalogar_con_ruedas(lista_vehiculos, 4)