import datetime

def agregar_inmueble(**kwargs): #las primeras son las reglas de validacion
        inmueble = {'name': name,'year':year,'metros':metros,'habitaciones':habitaciones, 'garage':True, 'zona': zona, 'estado':estado}
        if inmueble['year'] >= 2000 and inmueble['metros'] >= 60 and inmueble['habitaciones'] >= 2 and inmueble['zona'] in ['A','B','C']:
            inmuebles.append(inmueble)
            print(f"""
            Se ha ingresado un nuevo inmueble.
            {inmueble}
            """)

        else:
            print('No cumple con los requisitos minimos.')

#[{'year': 2023, 'metros': 80, 'habitaciones': 4, 'garage': True, 'zona': 'B', 'estado': 'Reservado'},{'year': 2003, 'metros': 72, 'habitaciones': 3, 'garage': True, 'zona': 'A', 'estado': 'Disponible'},
#{'year': 2023, 'metros': 80, 'habitaciones': 4, 'garage': True, 'zona': 'B', 'estado': 'Disponible'}]


def validar_flotante(cadena):
    longitud = len(cadena)
    contador = 0
    for letra in cadena:
        if letra in '0123456789.':
            contador += 1
    if contador == longitud:
        return True
    else:
        return False

def tiene_garaje(valor):
    if valor:
        return 1
    else:
        return 0

def calcular_precio(anio, metros, nro_habit, garage, zona):
    pass

def coeficiente_zona(zona):
    if zona == 'A':
        return 1
    elif zona == 'B':
        return 1.5
    else:
        return 2

disponibles =[]
def precio_inmueble(presupuesto, inmuebles): #presupuesto es un input e inmuebles la lista gral.
    for inmueble in inmuebles:
        si_garaje = 1500 if inmueble['garaje'] else 0
        antiguedad = 2023 - inmueble['year']
        lista = {'inmueble': inmueble['name'] , 'precio': inmueble['precio']}
        precio = ((inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 + si_garaje) * (1-antiguedad/100 )) * 1.5
        if precio <= presupuesto and inmueble['estado'] in ['Disponible', 'Reservado']:
            lista['name'] = inmueble['name']
            lista['precio'] = precio
            disponibles.append(lista)

def buscar_inmueble(inmuebles,precio_buscado):
    inmuebles_resultado = list()
    fecha_hoy = datetime.datetime.now()
    anio_hoy = fecha_hoy.year

    #Imprimiendo encabezado del listado resultado de la busqueda de inmuebles
    print('------------------------------------------------------------------------------------')
    print('| Nombre       | Metros  | Habitaciones | Garage | Zona | Estado      | Precio     |')
    print('------------------------------------------------------------------------------------')
    
    for inmueble in inmuebles:
        v_nombre = 'Propiedad ' + str(inmuebles.index(inmueble) + 1)
        v_anio = inmueble['year']
        v_metros = inmueble['metros']
        v_habitaciones = inmueble['habitaciones']
        v_garage = tiene_garaje(inmueble['garaje'])
        v_zona = inmueble['zona']
        v_coef_zona = coeficiente_zona(v_zona)
        v_estado = inmueble['estado']
        v_precio = (v_metros * 100 + v_habitaciones * 500 + v_garage * 1500) * (1 - (anio_hoy - v_anio) / 100) * v_coef_zona
        
        inmueble_result = {'year':v_anio,'metros':v_metros,'habitaciones':v_habitaciones, 'garage':True, 'zona': zona, 'estado':estado}
        inmueble_result.update({'precio': v_precio})
        if v_precio <= precio_buscado and v_estado in ('Disponible', 'Reservado'):
            
            print(f'| {v_nombre.ljust(13)}|{str(v_metros).rjust(8)} |{str(v_habitaciones).center(14)}|{str(bool(v_garage)).center(8)}|{v_zona.center(6)}| {v_estado.ljust(12)}|',end = ' ')
            print(str('${:,.2f}'.format(v_precio)).rjust(11)+'|')
            print('------------------------------------------------------------------------------------')

def listar(inmuebles): 
    contador = 0    #uso para poner con items
    for inmueble in inmuebles:
        nombre = inmueble['name']
        print(f'{contador} : {nombre}')
        contador += 1

def lista_deinmuebles(inmuebles):
    contador = 1    #uso para poner con items
    for inmueble in inmuebles:
        nombre = inmueble['name']
        print(f'{contador} : {nombre}.  Año: {inmueble["year"]}.  Metros: {inmueble["metros"]}.  Habitaciones: {inmueble["habitaciones"]}. Zona: {inmueble["zona"]}')
        contador += 1


def cambiar_estado(inmuebles):
    listar(inmuebles)
    indice = int(input('Introduce el índice del inmueble cuyo estado quieres cambiar: '))
    if 0 <= indice < len(inmuebles):
        estado = input('Introduce el nuevo estado del inmueble (Disponible/Reservado/Vendido): ')
        if estado not in ['Disponible', 'Reservado', 'Vendido']:
            print('El estado debe ser Disponible, Reservado o Vendido')
            return
        inmuebles[indice]['estado'] = estado
5
def eliminar_inmueble(inmuebles): #para_borrar
    listar(inmuebles)
    para_borrar = int(input('Ingrese la posicion del inmueble a borrar: '))
    inmuebles.pop(para_borrar)
    print(inmuebles)

#inmuebles = []  #lista para agregar inmuebles
inmuebles = [{'name': 'Inmueble 1', 'year': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'name': 'Inmueble 2', 'year': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'name': 'Inmueble 3', 'year': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'name': 'Inmueble 4', 'year': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'name': 'Inmueble 5', 'year': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]

while True:    
    print(f"""
    Inmobiliaria
    **********************
    1 - Ingresar Inmueble
    2 - Cambiar Estado de Inmueble
    3 - Eliminar Inmueble
    4 - Imprimir Lista
    5 - Busqueda de inmuebles
    6 - Salir
    **********************
    """)

    

    #### Datos a ingresar

    accion_usuario = int(input('Ingrese una opcion: '))

    if accion_usuario == 1:
        print('Ingresar datos del inmueble: ')
        name = input('Nombre: ')
        year = int(input('Año: '))
        metros = int(input('Metros: '))
        habitaciones = int(input('Habitaciones: '))
        garaje = input('¿Tiene garaje el inmueble? (s/n): ').lower() == 's'
        zona = input('Zona: ')
        estado = input('Estado (Disponible, Reservado, Vendido): ')
        agregar_inmueble()
        #print(inmuebles)

    if accion_usuario == 2:
        cambiar_estado(inmuebles)
        
    if accion_usuario == 3:
        eliminar_inmueble(inmuebles)
        
    if accion_usuario == 4:
        print('Lista de Inmuebles')
        lista_deinmuebles(inmuebles)
        
    if accion_usuario == 5:
        buscando = True
        while buscando:
            valor = input('Ingrese un precio para la búsqueda: ')
            if validar_flotante(valor):
                precio_buscado = float(valor)
                buscar_inmueble(inmuebles,precio_buscado)
                resultado = 'Inmueble a la vista' 
                buscando = False
            else:
                otra_vez = input('PRECIO NO VÁLIDO. Desea intentar con otro precio? (S): ').upper()
                if otra_vez == 'S':
                    continue
                else:
                    resultado = 'Inmueble no encontrado'
                    buscando = False
        print(resultado)


    if accion_usuario == 6:
        exit()
         

    
            



