def buscar_inmuebles(lista_inmuebles, presupuesto):
    inmuebles_encontrados = []
    
    for inmueble in lista_inmuebles:
        if (inmueble['estado'] in ['Disponible', 'Reservado'] and
                inmueble['precio'] <= presupuesto):
            inmuebles_encontrados.append(inmueble)
            return inmuebles_encontrados
def calcular_precio(inmueble):
    zona = inmueble['zona']
    metros = inmueble['metros']
    habitaciones = inmueble['habitaciones']
    antiguedad = 2023 - inmueble['año']
    garaje = 1 if inmueble['garaje'] else 0
    
    if zona == 'A':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100)
    elif zona == 'B':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 1.5
    elif zona == 'C':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 2
    return precio
#1
def agregar_inmueble(lista_inmuebles, inmueble):
    if inmueble['zona'] not in ['A', 'B', 'C']:
        print("Error: La zona del inmueble no es válida.")
        return
    
    if inmueble['estado'] not in ['Disponible', 'Reservado', 'Vendido']:
        print("Error: El estado del inmueble no es válido.")
        return
     if inmueble['año'] < 2000 or inmueble['metros'] < 60 or inmueble['habitaciones'] < 2:
        print("Error: El inmueble no cumple con las reglas de validación.")
        return
    
    inmueble['precio'] = calcular_precio(inmueble)
    lista_inmuebles.append(inmueble)
    print("Inmueble agregado con éxito.")
#2
def editar_inmueble(lista_inmuebles, indice, nuevos_datos):
    if indice < 0 or indice >= len(lista_inmuebles):
        print("Error: El índice del inmueble no es válido.")
        return
    
    inmueble = lista_inmuebles[indice]
    
    if 'zona' in nuevos_datos and nuevos_datos['zona'] not in ['A', 'B', 'C']:
        print("Error: La zona del inmueble no es válida.")
        return
    if 'estado' in nuevos_datos and nuevos_datos['estado'] not in ['Disponible', 'Reservado', 'Vendido']:
        print("Error: El estado del inmueble no es válido.")
        return
    if 'año' in nuevos_datos and nuevos_datos['año'] < 2000:
        print("Error: El año del inmueble no es válido.")
        return
    if 'metros' in nuevos_datos and nuevos_datos['metros'] < 60:
        print("Error: Los metros del inmueble no son válidos.")
        return
    if 'habitaciones' in nuevos_datos and nuevos_datos['habitaciones'] < 2:
        print("Error: El número de habitaciones del inmueble no es válido.")
        return
    
    inmueble.update(nuevos_datos)
    print("Inmueble editado con éxito.")

#3
def eliminar_inmueble(lista_inmuebles, indice):
    if indice < 0 or indice >= len(lista_inmuebles):
        print("Error: El inmueble no esta disponible.")

# Ejemplo de uso
inmuebles = [
    {'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
    {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
    {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
    {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
    {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
]