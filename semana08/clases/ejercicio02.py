class Vehiculo:
    def __init__(self, color, ruedas, nombre):
        self.color = color
        self.ruedas = ruedas
        self.nombre = nombre
    
    def __str__(self):
        return self.nombre
    
    def mostrar_atributos(self):
        for i in vars(self).items():
            print(f'{i[0].capitalize()} => {i[1]}')
    
    def mostrar_atributos1(self):
        for x, y in vars(self).items():
            print(x, y)
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, nombre, velocidad, cilindrada):
        super().__init__(color, ruedas, nombre)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, nombre, tipo):
        super().__init__(color, ruedas, nombre)
        self.tipo = tipo

class Camioneta(Vehiculo):
    def __init__(self, color, ruedas, nombre, carga):
        super().__init__(color, ruedas, nombre)
        self.carga = carga

class Motocicleta(Vehiculo):
    def __init__(self, color, ruedas, nombre, velocidad, cilindrada):
        super().__init__(color, ruedas, nombre)    
        self.velocidad = velocidad
        self.cilindrada = cilindrada

gol = Coche('Rojo', 4, 'Gol Trend', 160, 1.4)
hilux = Camioneta('Gris', 4, 'Ganzoo', 200)
mountain = Bicicleta('Negra', 2, 'Trek', 'Mountain Bike')
ducatti = Motocicleta('Blanca', 2,'Scrambler', 200, 1000)

lista_vehiculos = [gol, hilux, mountain, ducatti]
for i in lista_vehiculos:
    print(f"Vehiculo {i} - Clase: {type(i).__name__}")

gol.mostrar_atributos1()