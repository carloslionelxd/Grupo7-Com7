import datetime

# Determinación del año actual ==========
FECHA_HOY = datetime.datetime.now()
ANIO_HOY = FECHA_HOY.year
# Fin Determinación del año actual ======

registro_unico = 0 # Para nombrar los registros de las distintas propiedades

def agregar_inmueble(**kwargs): #las primeras son las reglas de validacion
    inmueble = {'name': name,
                'year':year,
                'metros':metros,
                'habitaciones':habitaciones, 
                'garage':garaje, 
                'zona': zona, 
                'estado': estado}
        
    inmuebles.append(inmueble)
    print('Se ha ingresado un nuevo inmueble.')
    print(f'{inmueble}')

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
     
# Fin validar tipo de datos=============================

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

# Inicio Funciones adicionales =========================

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

# Fin Funciones adicionales =========================

# Inicio Funciones principales=======================
disponibles =[]
def precio_inmueble(presupuesto, inmuebles): #presupuesto es un input e inmuebles la lista gral.
    for inmueble in inmuebles:
        si_garaje = 1500 if inmueble['garaje'] else 0
        antiguedad = ANIO_HOY - inmueble['year']
        lista = {'inmueble': inmueble['name'] , 'precio': inmueble['precio']}
        precio = ((inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 + si_garaje) * (1-antiguedad/100 )) * 1.5
        if precio <= presupuesto and inmueble['estado'] in ['Disponible', 'Reservado']:
            lista['name'] = inmueble['name']
            lista['precio'] = precio
            disponibles.append(lista)

def buscar_inmueble(inmuebles,precio_buscado):
    inmuebles_resultado = list()

    #Imprimiendo encabezado del listado resultado de la busqueda de inmuebles
    print('--------------------------------------------------------------------------------------------')
    print('| Nombre       | Año  |  Metros  | Habitaciones | Garage | Zona | Estado      | Precio     |')
    print('--------------------------------------------------------------------------------------------')
    
    #Preparamos variables para mostrar en cada registro con formato adecuado
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
            
            print(f'| {v_nombre.ljust(13)}|{str(v_anio).center(6)}|{str(v_metros).rjust(9)} |{str(v_habitaciones).center(14)}|{str(bool(v_garage)).center(8)}|{v_zona.center(6)}| {v_estado.ljust(12)}|',end = ' ')
            print(str('${:,.2f}'.format(v_precio)).rjust(11)+'|')
            print('--------------------------------------------------------------------------------------------')
            inmuebles_resultado.append(inmueble_result)
    return inmueble_result # Devolvemos la lista de los registros que cumplen las condiciones con el precio incluido
    

def listar(inmuebles): 
    contador = 0    #uso para poner con items
    for inmueble in inmuebles:
        nombre = inmueble['name']
        estado = inmueble['estado']
        print(f'{contador} : {nombre} {estado} ')
        contador += 1

def lista_deinmuebles(inmuebles):
    contador = 1    #uso para poner con items
    for inmueble in inmuebles:
        nombre = inmueble['name']
        print(f'{contador} : {nombre}.  Año: {inmueble["year"]}.  Metros: {inmueble["metros"]}.  Habitaciones: {inmueble["habitaciones"]}. Zona: {inmueble["zona"]}. Estado: {inmueble["estado"]}')
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

def eliminar_inmueble(inmuebles): #para_borrar
    listar(inmuebles)
    para_borrar = int(input('Ingrese la posicion del inmueble a borrar: '))
    inmuebles.pop(para_borrar)
    print(inmuebles)

# Fin Funciones principales=======================

# Menu principal del sistema de inmobiliaria======

inmuebles = []  #lista para agregar inmuebles

while True:    
    print(f"""
INMOBILIARIA - MENU DE OPCIONES
*******************************
1 - Ingresar Inmueble
2 - Cambiar Estado de Inmueble
3 - Eliminar Inmueble
4 - Imprimir Lista
5 - Busqueda de inmuebles
6 - Salir
*******************************
    """)

    

    #### Datos a ingresar

    accion_usuario = int(input('Ingrese una opcion: '))

    if accion_usuario == 1:
        proceso_ingreso = True

        while proceso_ingreso:
            print('Ingresar datos del inmueble: ')
            print('----------------------------')
            name = 'Propiedad ' + str(registro_unico + 1)
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

            garaje = input('Tiene Garage? (Ingrese el Nro: 1 = SI, 0 = NO):')
            if validar_booleano(garaje):
                garaje = bool(garaje)
            else:
                continue

            zona = input('Zona (A, B o C): ')
            if validar_zona(zona):
                zona = zona.upper()
            else:
                continue

            estado = input('Estado (Disponible, Reservado, Vendido): ')
            if validar_estado(estado):
                estado = estado.lower().capitalize()
            else:
                continue

            agregar_inmueble()  # Agregamos el registro del inmueble a la lista
            registro_unico += 1 # Incrementamos el nro de registro para nombrar al posible siguiente registro
            
            otro = input('Desea ingresar otra propiedad (S para continuar):')
            if otro.isalpha() and otro.upper() == 'S':
                continue
            else:
                proceso_ingreso = False

    
    if accion_usuario == 2:
        if len(inmuebles) == 0:
            print('No existen registros para editar.')
            continue
        cambiar_estado(inmuebles)
        
    if accion_usuario == 3:
        if len(inmuebles) == 0:
            print('No existen registros para borrar.')
            continue
        eliminar_inmueble(inmuebles)
        
    if accion_usuario == 4:
        if len(inmuebles) == 0:
            print('No existen registros para listar.')
            continue

        print('Lista de Inmuebles')
        lista_deinmuebles(inmuebles)
        
        
    if accion_usuario == 5:
        if len(inmuebles) == 0:
            resultado = 'No existen registros para buscar.'
            buscando = False
        else:
            buscando = True

        while buscando:
            valor = input('Ingrese un precio para la búsqueda: ')
            if validar_flotante(valor):
                precio_buscado = float(valor)
                buscar_inmueble(inmuebles,precio_buscado)
                resultado = 'Búsqueda finalizada' 
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
         

# INTEGRANTES

# Hugo Agustin Albertini
# Carlos Lionel Barboza
# Héctor Raúl Mansilla
# Janna Yael Sanchez
# Marcelo Gomez Armoa
# Gianfranco Manassi Mendivil
# Nallma Rodriguez 
# Monica Mansilla
# Gabriel Leandro Fernández