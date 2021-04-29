# informe_funciones.py
import csv
from fileparse import parse_csv
from pprint import pprint

LISTA_PRECIOS = '../Data/precios.csv'
CAMION = '../Data/camion.csv'

#--------------------------------------------------------------------------------------------------------------------------
# Ejercicio 2.16
# Modificado ejercicio 6.11

def leer_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as filas:
        return parse_csv(filas, types = [str, int, float])
#--------------------------------------------------------------------------------------------------------------------------
# Ejercicio 2.17
# Modificado ejercicio 6.11

def leer_precios(nombre_archivo):
    with open(nombre_archivo, 'rt') as filas:
        return dict(parse_csv(filas, types = [str, float], has_headers = False))
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
# Modificacion ejercicio 6.4 (y 6.5)

def imprimir_informe(informe):
    """
    Recibe un informe y lo imprime en pantalla, formateado como tabla
    """
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio = '$' + str(round(precio,2))
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)

# Ejercicio 7.2 y 7.3

def main(parametros):
    informe_camion(parametros[1], parametros[2])


if __name__ == '__main__':
    import sys
    main(sys.argv)
#--------------------------------------------------------------------------------------------------------------------------
"""
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

#costo_total, ganancia_total = analizar_camion(leer_camion(CAMION))
# print(f'Costo total: {costo_total}\nGanancias: {ganancia_total}\nBalance: {round(ganancia_total - costo_total, 2)}')

#--------------------------------------------------------------------------------------------------------------------------


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