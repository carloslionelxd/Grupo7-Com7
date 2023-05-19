def seleccionar_inmuebles(inmuebles, año):
    seleccion = []
    for inmueble in inmuebles:
        if inmueble['estado'] == 'Disponible' and inmueble['año'] == año:
            seleccion.append(inmueble)
    return seleccion

def agregar_inmueble(inmuebles):
    año = int(input('Introduce el año del inmueble: '))
    if año < 2000:
        print('El año debe ser mayor o igual a 2000')
        return
    metros = int(input('Introduce los metros cuadrados del inmueble: '))
    if metros < 60:
        print('Los metros cuadrados deben ser mayores o iguales a 60')
        return
    habitaciones = int(input('Introduce el número de habitaciones del inmueble: '))
    if habitaciones < 2:
        print('El número de habitaciones debe ser mayor o igual a 2')
        return
    garaje = input('¿Tiene garaje el inmueble? (s/n): ').lower() == 's'
    zona = input('Introduce la zona del inmueble (A/B/C): ')
    if zona not in ['A', 'B', 'C']:
        print('La zona debe ser A, B o C')
        return
    estado = input('Introduce el estado del inmueble (Disponible/Reservado/Vendido): ')
    if estado not in ['Disponible', 'Reservado', 'Vendido']:
        print('El estado debe ser Disponible, Reservado o Vendido')
        return
    inmueble = {'año': año, 'metros': metros, 'habitaciones': habitaciones, 'garaje': garaje, 'zona': zona, 'estado': estado}
    inmuebles.append(inmueble)
    volver_al_menu = input('Inmueble agregado con éxito. ¿Desea volver al menú principal? (s/n): ').lower() == 's'
    if volver_al_menu:
        return True

def editar_inmueble(inmuebles):
    indice = int(input('Introduce el índice del inmueble que quieres editar: '))
    if 0 <= indice < len(inmuebles):
        año = int(input('Introduce el nuevo año del inmueble: '))
        if año < 2000:
            print('El año debe ser mayor o igual a 2000')
            return
        metros = int(input('Introduce los nuevos metros cuadrados del inmueble: '))
        if metros < 60:
            print('Los metros cuadrados deben ser mayores o iguales a 60')
            return
        habitaciones = int(input('Introduce el nuevo número de habitaciones del inmueble: '))
        if habitaciones < 2:
            print('El número de habitaciones debe ser mayor o igual a 2')
            return
        garaje = input('¿Tiene garaje el inmueble? (s/n): ').lower() == 's'
        zona = input('Introduce la nueva zona del inmueble (A/B/C): ')
        if zona not in ['A', 'B', 'C']:
            print('La zona debe ser A, B o C')
            return
        estado = input('Introduce el nuevo estado del inmueble (Disponible/Reservado/Vendido): ')
        if estado not in ['Disponible', 'Reservado', 'Vendido']:
         print('El estado debe ser Disponible, Reservado o Vendido')
         return
        inmuebles[indice] = {'año': año, 'metros': metros, 'habitaciones': habitaciones, 'garaje': garaje, 'zona': zona, 'estado': estado}
        volver_al_menu = input('Inmueble editado con éxito. ¿Desea volver al menú principal? (s/n): ').lower() == 's'
        if volver_al_menu:
         return True

def eliminar_inmueble(inmuebles):
    indice = int(input('Introduce el índice del inmueble que quieres eliminar: '))
    if 0 <= indice < len(inmuebles):
        del inmuebles[indice]
        volver_al_menu = input('Inmueble eliminado con éxito. ¿Desea volver al menú principal? (s/n): ').lower() == 's'
        if volver_al_menu:
            return True

def cambiar_estado(inmuebles):
    indice = int(input('Introduce el índice del inmueble cuyo estado quieres cambiar: '))
    if 0 <= indice < len(inmuebles):
        estado = input('Introduce el nuevo estado del inmueble (Disponible/Reservado/Vendido): ')
        if estado not in ['Disponible', 'Reservado', 'Vendido']:
            print('El estado debe ser Disponible, Reservado o Vendido')
            return
        inmuebles[indice]['estado'] = estado
        volver_al_menu = input('Estado del inmueble cambiado con éxito. ¿Desea volver al menú principal? (s/n): ').lower() == 's'
        if volver_al_menu:
            return True

def buscar_inmuebles(inmuebles, precio_maximo):
    seleccion = []
    año_actual = 2023
    for inmueble in inmuebles:
        metros = inmueble['metros']
        habitaciones = inmueble['habitaciones']
        garaje = 1500 if inmueble['garaje'] else 0
        antiguedad = año_actual - inmueble['año']
        zona = inmueble['zona']
        estado = inmueble['estado']
        if zona == 'A':
            precio = (metros * 100 + habitaciones * 500 + garaje) * (1 - antiguedad / 100)
        elif zona == 'B':
            precio = (metros * 100 + habitaciones * 500 + garaje) * (1 - antiguedad / 100) * 1.5
        elif zona == 'C':
            precio = (metros * 100 + habitaciones * 500 + garaje) * (1 - antiguedad / 100) * 2
        if precio <= precio_maximo and estado in ['Disponible', 'Reservado']:
         inmueble_con_precio = inmueble.copy()
    inmueble_con_precio['precio'] = precio
    seleccion.append(inmueble_con_precio)
    return seleccion

def menu(inmuebles):
    while True:
        print('1. Seleccionar inmuebles')
        print('2. Agregar inmueble')
        print('3. Editar inmueble')
        print('4. Eliminar inmueble')
        print('5. Cambiar estado de inmueble')
        print('6. Buscar inmuebles por presupuesto')
        print('7. Salir')
        opcion = int(input('Elige una opción: '))
        if opcion == 1:
            año = int(input('Introduce el año de los inmuebles que quieres seleccionar: '))
            seleccion = seleccionar_inmuebles(inmuebles, año)
            print('Inmuebles seleccionados:')
            for inmueble in seleccion:
                print(f"Año: {inmueble['año']}")
                print(f"Metros: {inmueble['metros']}")
                print(f"Habitaciones: {inmueble['habitaciones']}")
                print(f"Garaje: {'Sí' if inmueble['garaje'] else 'No'}")
                print(f"Zona: {inmueble['zona']}")
                print(f"Estado: {inmueble['estado']}")
                print()
            volver_al_menu = input('¿Desea volver al menú principal? (s/n): ').lower() == 's'
            if volver_al_menu:
                continue
        elif opcion == 2:
            volver_al_menu = agregar_inmueble(inmuebles)
            if volver_al_menu:
                continue
        elif opcion == 3:
            volver_al_menu = editar_inmueble(inmuebles)
            if volver_al_menu:
                continue
        elif opcion == 4:
            volver_al_menu = eliminar_inmueble(inmuebles)
            if volver_al_menu:
                continue
        elif opcion == 5:
            volver_al_menu = cambiar_estado(inmuebles)
            if  volver_al_menu:
                continue
        elif opcion == 6:
             precio_maximo = int(input('Introduce el presupuesto máximo: '))
        seleccion = buscar_inmuebles(inmuebles, precio_maximo)
        print('Inmuebles seleccionados:')
        for inmueble in seleccion:
                print(f"Año: {inmueble['año']}")
                print(f"Metros: {inmueble['metros']}")
                print(f"Habitaciones: {inmueble['habitaciones']}")
                print(f"Garaje: {'Sí' if inmueble['garaje'] else 'No'}")
                print(f"Zona: {inmueble['zona']}")
                print(f"Estado: {inmueble['estado']}")
                print(f"Precio: {inmueble['precio']}")
                print()
        volver_al_menu = input('¿Desea volver al menú principal? (s/n): ').lower() == 's'
        if volver_al_menu:
                continue
        elif opcion == 7:
            break
inmuebles = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
        {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
        {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
        {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
        {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]
menu(inmuebles)


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
