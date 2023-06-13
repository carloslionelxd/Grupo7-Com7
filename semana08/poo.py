class Persona:
    def __init__(self, nombre, edad, domicilio):
        self.nombre = nombre
        self.edad = edad
        self.domicilio = domicilio
        #self.__domicilio = _Persona__domicilio

    def saludar(self):
        print(f'Mi nombre es {self.nombre}')

    def correr(self):
        print(f'{self.nombre} está corriendo')

persona1 = Persona('Carlos', 30, 'Calle 10 222')
persona2 = Persona('Maria', 38, 'Las Heras 890')

persona1.saludar()
persona2.correr()