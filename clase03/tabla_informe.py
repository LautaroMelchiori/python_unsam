import csv
from pprint import pprint

LISTA_PRECIOS = '../Data/precios.csv'
CAMION = '../Data/fecha_camion.csv'

#--------------------------------------------------------------------------------------------------------------------------
# Ejercicio 2.16

def leer_camion(nombre_archivo):
    informe = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            try:
                lote = {'nombre' : record['nombre'],
                        'cajones' : int(record['cajones']),
                        'precio' : float(record['precio'])}
                informe.append(lote)
            # manejamos el error que puede surgir si hay una linea con datos faltantes
            except IndexError:
                continue
    return informe
#--------------------------------------------------------------------------------------------------------------------------
# Ejercicio 2.17

def leer_precios(nombre_archivo):
    listado_de_precios = {}
    with open(nombre_archivo, 'rt') as f:
         rows = csv.reader(f)
         for row in rows:
             try:
                 listado_de_precios[row[0]] = float(row[1])
             # manejamos el error que puede surgir si aparece una linea vacia
             except IndexError:
                 continue
    return listado_de_precios
#--------------------------------------------------------------------------------------------------------------------------
# Ejercicio 3.13

def hacer_informe(lotes, precios):
    informe = []
    for lote in lotes:
        fruta = lote['nombre']
        cajones = lote['cajones']
        precio_produccion = lote['precio']
        cambio = precios[fruta] - precio_produccion
        informe.append((fruta, cajones, precio_produccion, cambio))
    return informe

"""
Ejercicio 3.14

camion = leer_camion(CAMION)
precios = leer_precios(LISTA_PRECIOS)
informe = hacer_informe(camion, precios)

for nombre, cajones, precio, cambio in informe:
    print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')
"""
#--------------------------------------------------------------------------------------------------------------------------
# Ejercicio 3.15 (y 3.16)

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print('---------- ---------- ---------- ----------')
camion = leer_camion(CAMION)
precios = leer_precios(LISTA_PRECIOS)
informe = hacer_informe(camion, precios)

for nombre, cajones, precio, cambio in informe:
    precio = '$' + str(round(precio,2))
    print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')

#--------------------------------------------------------------------------------------------------------------------------
# Ejercicio 2.18


# Esta funcion toma la informacion de un camion y calcula su coste total y su ganancia por ventas
def analizar_camion(camion):
    costo = 0.0
    ganancias = 0.0
    listado_precios_venta = leer_precios(LISTA_PRECIOS)

    for lote in camion:
        fruta = lote['nombre']
        cantidad_cajones = lote['cajones']
        precio = lote['precio']
        precio_venta = listado_precios_venta[fruta]
        costo += cantidad_cajones * precio
        ganancias += cantidad_cajones * precio_venta

    return costo, ganancias

costo_total, ganancia_total = analizar_camion(leer_camion(CAMION))

# print(f'Costo total: {costo_total}\nGanancias: {ganancia_total}\nBalance: {round(ganancia_total - costo_total, 2)}')

#--------------------------------------------------------------------------------------------------------------------------



"""
----------------------------------------------------------
Ejercicio 2.15 

def leer_camion(nombre_archivo):
    informe = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        next(f)
        for row in rows:
            lote = (row[0], int(row[1]), float(row[2]))
            informe.append(lote)
    pprint(informe)
    return informe
----------------------------------------------------------         
"""