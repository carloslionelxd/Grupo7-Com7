import datetime

def agregar_inmueble(**kwargs): #las primeras son las reglas de validacion
        inmueble = {'year':year,'metros':metros,'habitaciones':habitaciones, 'garage':True, 'zona': zona, 'estado':estado}
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

def tiene_garage(valor):
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
        v_garage = tiene_garage(inmueble['garage'])
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


inmuebles = []  #lista para agregar inmuebles

while True:    
    print(f"""
    Inmobiliaria
    **********************
    1 - Ingresar Inmueble
    2 - Editar Inmueble
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
        year = int(input('Año: '))
        metros = int(input('Metros: '))
        habitaciones = int(input('Habitaciones: '))
        garage = True
        zona = input('Zona: ')
        estado = input('Estado (Disponible, Reservado, Vendido): ')
        agregar_inmueble()
        #print(inmuebles)


    if accion_usuario == 4:
        for inmueble in inmuebles: #se podria usar el indice para acceder cuando se lo quiera editar?
            print('-'*20)
            print('Lista de Inmuebles')
            print(f"""
            Indice: {inmuebles.index(inmueble)}
            Year: {inmueble['year']}
            Metros: {inmueble['metros']}
            Habitaciones: {inmueble['habitaciones']}
            Zona: {inmueble['zona']}
            Estado: {inmueble['estado']}

            """)

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
         

    
            



