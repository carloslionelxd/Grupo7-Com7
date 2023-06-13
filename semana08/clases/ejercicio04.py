class Tiempo:
    def __init__(self, hora, minutos = 0, segundos = 0):
        self.__hora = hora
        self.__minutos = minutos
        self.__segundos = segundos
    
    def modificar_hora(self):
        hora = input('Ingrese la hora:')
        minutos = input('Ingrese los minutos:')
        segundos = input('Ingrese los segundos:')
        self.__hora = hora
        self.__minutos = minutos
        self.__segundos = segundos
    
    def mostrar_hora(self):
        #return print(f'Hora: {self.__hora}\nMinutos: {self.__minutos}\nSegundos: {self.__segundos}')
        return print(f'{self.__hora}:{self.__minutos}:{self.__segundos}')
    
reloj = Tiempo(15,20)
reloj.mostrar_hora()
reloj.modificar_hora()
reloj.mostrar_hora()