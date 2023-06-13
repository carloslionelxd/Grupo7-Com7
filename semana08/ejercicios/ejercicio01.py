class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f'Soy un vehículo de color {self.color} que tiene {self.ruedas} ruedas.'
    
    def mostrar_color(self):
        return self.color

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f'Soy un coche {self.color} de {self.ruedas} ruedas con Vel.Max de {str(self.velocidad)} Km/h y {str(self.cilindrada)}L de cilindrada.'

    def mostrar_velocidad(self):
        return self.velocidad

# Instancias        
soa = Vehiculo('Verde', 4)
lui = Vehiculo('Negro', 4)
ae = Vehiculo('azul', 4)

soa266 = Coche('Verde', 4, 160, 1.6)
lui702 = Coche('Negro', 4, 180, 1.6)
ae003nj = Coche('azul', 4, 220, 1.5)
#
print(soa)
print(lui)
print(f'El color del vehículo es {soa.mostrar_color()}')

print(lui702)
print(f'El coche tiene una velocidad max. de {ae003nj.mostrar_velocidad()} km/h')