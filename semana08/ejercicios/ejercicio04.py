class Tiempo:
    def __init__(self, hora, minuto = 0, segundo = 0):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo

    def set_hora(self, hora):
        self.__hora = hora

    def set_minuto(self, minuto):
        self.__minuto = minuto

    def set_segundo(self, segundo):
        self.__segundo = segundo

    def __str__(self):
        return f'Tiempo = {self.__hora}:{self.__minuto}:{self.__segundo}'
    

horas = int(input('Ingrese la hora: '))
minutos = int(input('Ingrese los minutos: '))
segundos = int(input('Ingrse los segundos: '))

tiempo1 = Tiempo(horas, minutos, segundos)
print(f'Ahora es: {tiempo1}')

tiempo1.set_hora(23)
print(tiempo1)