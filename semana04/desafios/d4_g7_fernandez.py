'''
Se te pide construir un programa que permita:
    Agregar, editar y eliminar inmuebles a la lista.
        Las funciones deben ajustarse al formato de lista y reglas de validación.

    Cambiar el estado de un inmueble, sin modificar sus demás datos.
        Las funciones deben ajustarse al formato de lista y reglas de validación.

    Hacer búsqueda de inmuebles en función de un presupuesto dado.
        La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con
        los inmuebles cuyo precio sea menor o igual que el dado y el estado sea Disponible o
        Reservado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada
        diccionario con el precio del inmueble, donde el precio de un inmueble se calcula con las
        reglas de precio en función de la zona.
'''

'''
Notese que la consigna nos da ciertas "reglas", que en realidad es una re pista sobre como almacenar los inmuebles 😉 
Nos pide que el usuario pueda modificar distintos valores de estos diccionarios que se almacenan en la lista, 
estas acciones debemos poder encapsularla en distinas funciones.
***Es decir definir una funcion para cada accion (agregar, editar, eliminar).***
'''
'''
El ultimo item, solicita definir una funcion que reciba como parametro la lista de inmuebles y un precio (dos parametros) y retorne una lista con los inmuebles 
que valen menos o igual que el precio pasado como argumento, y que al mismo tiempo tengan un estado de Disponible o Reservado.

Esta lista que devuelve la funcion de buscar, debe incorporar en el diccionario de cada inmuenle un par clave-valor adicional, que es el PRECIO. Notese que el precio
resulta del calculo dado en la consigna dependiendo de la zona.
Respecto a las REGLAS DE VALIDACION. Se refiere a que si el usuario ingresa por ejemplo un inmueble nuevo que NO sea la A, B o C, nos arroje una advertencia, 
y nos vuelva a solicitar.

Tambien que los unicos estados posibles que pueda tener un inmueble sean RESERVADO, DISPONIBLE, VENDIDO.

Y que NO se pueda agregar o modificar inmuebles para que estos sean anteriores al 2000, con menos de 60mts2, o con menos de dos habitaciones.
'''

#1--------------------------------------------------------------------
def agregar_inmueble(lista_inmuebles, inmueble):
    if validar_inmueble(inmueble):
        lista_inmuebles.append(inmueble)
        print("Inmueble agregado correctamente.")
    else:
        print("El inmueble no cumple con las reglas de validación.")

def editar_inmueble(lista_inmuebles, indice, nuevo_inmueble):
    if validar_inmueble(nuevo_inmueble):
        if indice >= 0 and indice < len(lista_inmuebles):
            lista_inmuebles[indice] = nuevo_inmueble
            print("Inmueble editado correctamente.")
        else:
            print("Índice de inmueble inválido.")
    else:
        print("El inmueble no cumple con las reglas de validación.")

def eliminar_inmueble(lista_inmuebles, indice):
    if indice >= 0 and indice < len(lista_inmuebles):
        del lista_inmuebles[indice]
        print("Inmueble eliminado correctamente.")
    else:
        print("Índice de inmueble inválido.")
#1--------------------------------------------------------------------

#2--------------------------------------------------------------------
def cambiar_estado(lista_inmuebles, indice, nuevo_estado):
    if indice >= 0 and indice < len(lista_inmuebles):
        lista_inmuebles[indice]['estado'] = nuevo_estado
        print("Estado de inmueble cambiado correctamente.")
    else:
        print("Índice de inmueble inválido.")
#2--------------------------------------------------------------------

#3--------------------------------------------------------------------
def buscar_inmuebles(lista_inmuebles, presupuesto):
    inmuebles_encontrados = []
    for inmueble in lista_inmuebles:
        if inmueble['estado'] in ['Disponible', 'Reservado']:
            precio = calcular_precio(inmueble)
            if precio <= presupuesto:
                inmueble_actualizado = inmueble.copy()
                inmueble_actualizado['precio'] = precio
                inmuebles_encontrados.append(inmueble_actualizado)
    return inmuebles_encontrados
#3--------------------------------------------------------------------

def validar_inmueble(inmueble):
    if inmueble['zona'] not in ['A', 'B', 'C']: # si el inmueble no esta en la zona a, b ,c -> retorname falso 
        return False 
    if inmueble['estado'] not in ['Disponible', 'Reservado', 'Vendido']: # el inmueble debe tener alguno de los estados disponible, reservado o vendido
        return False
    if inmueble['año'] < 2000: # no se opera con inmuebles que preceden al año 2000
        return False
    if inmueble['metros'] < 60: # no se opera con inmuebles con menos a 60 metros
        return False
    if inmueble['habitaciones'] < 2: # no se opera con inmuebles con menos de 2 habitaciones
        return False
    return True

def calcular_precio(inmueble):
    antiguedad = 2023 - inmueble['año']
    metros = inmueble['metros']
    habitaciones = inmueble['habitaciones']
    garaje = inmueble['garaje']
    zona = inmueble['zona']

    if zona == 'A':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100)
    elif zona == 'B':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 1.5
    elif zona == 'C':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 2
    
    return precio

# Ejemplo de uso del programa
inmuebles = [
    {'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
    {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
    {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
    {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
    {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
]