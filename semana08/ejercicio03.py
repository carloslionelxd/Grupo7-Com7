class Triangulo:
    def __init__(self, lado1, lado2, lado3) :
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        return max(self.lado1, self.lado2, self.lado3)
    
    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return 'Equilatero'
        elif self.lado1 != self.lado2 != self.lado3:
            return 'Escaleno'
        else:
            return 'Isósceles'
    
triangulo1 = Triangulo(3,4,3)

print(f'El lado mayor es {triangulo1.lado_mayor()}')
print(f'El triangulo es {triangulo1.tipo_triangulo()}')
