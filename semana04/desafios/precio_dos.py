inmuebles =[{'name':'Inmueble3', 'year': 2015, 'metros': 90, 'habitaciones': 4, 'garaje': True, 'zona': 'B', 'estado': 'Reservado', 'precio':''},
              {'name':'Inmueble2', 'year': 2003, 'metros': 72, 'habitaciones': 3, 'garaje': False, 'zona': 'A', 'estado': 'Disponible', 'precio':''},
              {'name':'Inmueble1', 'year': 2015, 'metros': 120, 'habitaciones': 4, 'garaje': True, 'zona': 'B', 'estado': 'Disponible', 'precio':''}]

disponibles =[] #lista para poner los inmuebles que entran dentro del presupusto
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
            continue

def lista_precio(*args):
    contador = 1    #uso para poner con items
    print(f'Inmuebles disponibles para un presupuesto de $ {presupuesto}')
    for inmueble in disponibles:
        nombre = inmueble['name']
        precio = inmueble['precio']
        print(f'{contador} : {nombre}  ${precio}')
        contador += 1
        continue

presupuesto = 25000 #input entero
precio_inmueble(presupuesto,inmuebles)
lista_precio(presupuesto, disponibles)

