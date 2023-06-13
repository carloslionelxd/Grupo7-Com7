class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def __str__(self):
        return f'Lado1: {self.lado1} - Lado2: {self.lado2} - Lado3: {self.lado3}'
    
    def es_triangulo(self):
        if self.lado1 + self.lado2 > self.lado3 and\
           self.lado1 + self.lado3 > self.lado2 and\
           self.lado2 + self.lado3 > self.lado1:
            return True
        else:
            return False

    def triangulo_tipo(self):
        if self.es_triangulo():
            conjunto = set()
            conjunto = {self.lado1, self.lado2, self.lado3}
            if len(conjunto) == 1:
                tipo = 'equilatero'
            elif len(conjunto) == 2:
                tipo = 'isósceles'
            else:
                tipo = 'escaleno'
            return tipo
        else:
            return 'No es triángulo'

triangulo1 = Triangulo(4, 6, 2)
#print(triangulo1)
#print(triangulo1.es_triangulo())
print(triangulo1.triangulo_tipo())