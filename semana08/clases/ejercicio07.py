class Bebida:
    def __init__(self, id, litros, marca, precio):
        self.id = id
        self.litros = litros
        self.marca = marca
        self.precio = precio

    def obtener_precio(self):
        return self.precio
    
    def ver_info(self):
        print(f'Id: {self.id}')
        print(f'Litros: {self.litros}')
        print(f'Marca: {self.marca}')
        print(f'Precio: {self.precio}')
        



class AguaMineral(Bebida):
    def __init__(self, id, litros, marca, precio, origen):
        super().__init__(id, litros, marca, precio)
        self.origen = origen

class Gaseosa(Bebida):
    def __init__(self, id, litros, marca, precio, porcentaje_azucar, promocion = False):
        super().__init__(id, litros, marca, precio)
        self.porcentaje_azucar = porcentaje_azucar
        self.promocion = promocion

    def obtener_precio(self):
        if self.promocion:
            return self.precio * (1 - 0.1)
        return self.precio

class Almacen:
    def __init__(self):
        self.lista_bebidas = list()

    def agregar_bebida(self, bebida):
        if not isinstance(bebida, AguaMineral) and not isinstance(bebida, Gaseosa):
            print('El dato ingresado no es de la clase agua o gaseosa')
        
        for b in self.lista_bebidas:
            if b.id == bebida.id:
                print('ID EXISTENTE')
                return
        self.lista_bebidas.append(bebida)

    def obtener_total(self, marca = None):
        total = 0
        if marca == None:
            for bebida in self.lista_bebidas:
                total += bebida.obtener_precio()
        else:
            for bebida in self.lista_bebidas:
                total += bebida.obtener_precio()
        return total
    
    def eliminar_producto(self, id):
        for b in self.lista_bebidas:
            if b.id == id:
                self.lista_bebidas.remove(b)
                return
        print('No se encontro ID')

    def ver_info_almacen(self):
        for b in self.lista_bebidas:
            b.ver_info()

        


# Programa principal
almacen1 = Almacen()
bebida1 = AguaMineral(1, 2, 'Villavicencio', 250, 'Manantial')
bebida2 = Gaseosa(2, 3, 'Coca Cola', 700, 0.2, True)
bebida3 = AguaMineral(1, 2, 'Sierra de los Padres', 350, 'Manantial')
bebida4 = Gaseosa(2, 3, 'Sprite', 700, 0.2, True)
bebida5 = AguaMineral(1, 2, 'Villa del Sur', 300, 'Manantial')
bebida6 = Gaseosa(2, 3, 'Fanta', 700, 0.2)

