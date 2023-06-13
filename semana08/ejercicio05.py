class Producto:
    def __init__(self, nombre, cantidad_total):
        self.nombre = nombre
        self.cantidad_total = cantidad_total
    
    def calcular(self, cantidad_a_donar, *args):
        if cantidad_a_donar <= self.cantidad_total:
            cantidad_por_entidad = cantidad_a_donar // len(args)
            sobrante = cantidad_a_donar % len(args)
            print(f'Para cada entidad se destinará {cantidad_por_entidad} unidades.\nSobraron {sobrante} unidades para la proxima donacion.')
        else:
            print(f'Cantidad insuficiente. Solo tenes {self.cantidad_total}')

class Perecedero(Producto):
    def __init__(self, nombre, cantidad_total, dias_a_caducar):
        super().__init__(nombre, cantidad_total)
        self.dias_a_caducar = dias_a_caducar
    
    def calcular(self, cantidad_a_donar, *args):
        super().calcular(cantidad_a_donar, *args)
        if self.dias_a_caducar < 10:
            print(f'Le quedan {self.dias_a_caducar}. Tenes que donarlo hoy')
        elif self.dias_a_caducar <30:
            print(f'Le quedan {self.dias_a_caducar}. Tenes una semana)
    

class NoPerecedero(Producto):
    def __init__(self, nombre, cantidad_total, tipo):
        super().__init__(nombre, cantidad_total)
        self.tipo = tipo
    
    def calcular(self,)

producto1 = Perecedero('Leche', 20, 300)

producto1.calcular(10, 'Comedor 123', 'Hogar de niñas', 'Merendero La hora feliz')