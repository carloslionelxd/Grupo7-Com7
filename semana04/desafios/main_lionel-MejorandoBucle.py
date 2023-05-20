import datetime

# Determinación del año actual ==========
FECHA_HOY = datetime.datetime.now()
ANIO_HOY = FECHA_HOY.year
# Fin Determinación del año actual ======

def agregar_inmueble(**kwargs): #las primeras son las reglas de validacion
    inmueble = {'year':year,
                'metros':metros,
                'habitaciones':habitaciones, 
                'garage':garage, 
                'zona': zona, 
                'estado': estado}
        
    inmuebles.append(inmueble)
    print('Se ha ingresado un nuevo inmueble.')
    print(f'{inmueble}')

#[{'year': 2023, 'metros': 80, 'habitaciones': 4, 'garage': True, 'zona': 'B', 'estado': 'Reservado'},{'year': 2003, 'metros': 72, 'habitaciones': 3, 'garage': True, 'zona': 'A', 'estado': 'Disponible'},
#{'year': 2023, 'metros': 80, 'habitaciones': 4, 'garage': True, 'zona': 'B', 'estado': 'Disponible'}]

# Inicio Validación de campos ==========================

def validar_anio(anio):
    if validar_entero(anio):
        anio = int(anio)
        if anio >= 2000 and anio <= ANIO_HOY:
            return True
        else:
            print(f'El año debe estar comprendido entre 2000 y {ANIO_HOY}')
            return False
    else:
        print('Valor incorrecto para el año de construcción')
        return False
    
def validar_metros(metros):
    if validar_entero(metros):
        metros = int(metros)
        if metros >= 60:
            return True
        else:
            print('Metros no puede ser inferior a 60')
            return False
    else:
        print('Valor incorrecto para la superficie')
        return False

def validar_habitaciones(nro):
    if validar_entero(nro):
        habitaciones = int(nro)
        if habitaciones >= 2:
            return True
        else:
            print('El número de habitaciones no puede ser menor a 2')
            return False
    else:
        print('Valor incorrecto para el número de habitaciones')

def validar_zona(zona):
    zona = zona.upper()
    if zona in ('A', 'B', 'C'):
        return True
    else:
        print('Valor incorrecto para la zona')
        return False

def validar_estado(estado):
    estado = estado.lower().capitalize()
    if estado in ('Disponible', 'Reservado', 'Vendido'):
        return True
    else:
        print('Valor incorrecto para el estado')
        return False

# Fin validación de campos =============================

# Validar tipos de datos ===============================

def validar_entero(entero):
    if entero.isdigit():
        return True
    else:
        return False

def validar_booleano(valor):
    if validar_entero(valor):
        valor = int(valor)    
        if valor in (0,1):
            return True
        else:
            print('Error: Se esperaba un 0 o 1')
            return False
    else:
        print('Error: Se esperaba un valor entero')
        return False

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
    
# Fin validar tipo de datos============================

def tiene_garage(valor):
    if valor:
        return 1
    else:
        return 0

def coeficiente_zona(zona):
    if zona == 'A':
        return 1
    elif zona == 'B':
        return 1.5
    else:
        return 2

def buscar_inmueble(inmuebles,precio_buscado):
    inmuebles_resultado = list()

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
        v_precio = (v_metros * 100 + v_habitaciones * 500 + v_garage * 1500) * (1 - (ANIO_HOY - v_anio) / 100) * v_coef_zona
        
        inmueble_result = {'year':v_anio,'metros':v_metros,'habitaciones':v_habitaciones, 'garage':True, 'zona': zona, 'estado':estado}
        inmueble_result.update({'precio': v_precio})
        if v_precio <= precio_buscado and v_estado in ('Disponible', 'Reservado'):
            
            print(f'| {v_nombre.ljust(13)}|{str(v_metros).rjust(8)} |{str(v_habitaciones).center(14)}|{str(bool(v_garage)).center(8)}|{v_zona.center(6)}| {v_estado.ljust(12)}|',end = ' ')
            print(str('${:,.2f}'.format(v_precio)).rjust(11)+'|')
            print('------------------------------------------------------------------------------------')
            inmuebles_resultado.append(inmueble_result)
    return inmueble_result

# Menu principal del sistema de inmobiliaria============================================================
inmuebles = []  #lista para agregar inmuebles

while True:    
    print(f"""
Inmobiliaria - MENU
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
        proceso_ingreso = True

        while proceso_ingreso:
            print('Ingresar datos del inmueble: ')
            print('----------------------------')
            year = input('Año: ')
            if validar_anio(year):
                year = int(year)
            else:
                continue
            
            metros = input('Metros: ')
            if validar_metros(metros):
                metros = int(metros)
            else:
                continue

            habitaciones = input('Habitaciones: ')
            if validar_habitaciones(habitaciones):
                habitaciones = int(habitaciones)
            else:
                continue

            garage = input('Tiene Garage? (Ingrese el Nro: 1 = SI, 0 = NO):')
            if validar_booleano(garage):
                garage = bool(garage)
            else:
                continue

            zona = input('Zona: ')
            if validar_zona(zona):
                zona = zona.upper()
            else:
                continue

            estado = input('Estado (Disponible, Reservado, Vendido): ')
            if validar_estado(estado):
                estado = estado.lower().capitalize()
            else:
                continue

            agregar_inmueble()
            #print(inmuebles)
            otro = input('Desea ingresar otra propiedad (S para continuar):')
            if otro.isalpha() and otro.upper() == 'S':
                continue
            else:
                proceso_ingreso = False

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
         

    
            


