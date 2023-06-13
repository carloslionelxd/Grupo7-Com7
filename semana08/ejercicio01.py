class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def mostrar_atributos(self):
        for i in vars(self).items():
            print(f'{i[0].capitalize()} => {i[1]}')
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

coche1 = Coche('Rojo', 4, 220, 2000)

coche1.mostrar_atributos()