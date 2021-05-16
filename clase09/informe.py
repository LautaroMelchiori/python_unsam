# informe_funciones.py
import csv
from fileparse import parse_csv
from lote import Lote
#--------------------------------------------------------------------------------------------------------------------------
# Ejercicio 2.16
# Modificado ejercicio 6.11
# Modificado ejercicio 7.5
# Modificado ejercicio 9.4

def leer_camion(nombre_archivo):
    """
    Recibe el nombre de un archivo csv conteniendo la data de un camion
    Devuelve una lista de objetos Lote con cada lote del camion
    """
    with open(nombre_archivo, 'rt') as filas:
        lotes = parse_csv(filas, types = [str, int, float])
        return [Lote(lot['nombre'], lot['cajones'], lot['precio']) for lot in lotes]
#--------------------------------------------------------------------------------------------------------------------------
# Ejercicio 2.17
# Modificado ejercicio 6.11
# Modificado ejercicio 7.5

def leer_precios(nombre_archivo):
    with open(nombre_archivo, 'rt') as filas:
        return dict(parse_csv(filas, types = [str, float], has_headers = False))
#--------------------------------------------------------------------------------------------------------------------------
# Ejercicio 3.13

def hacer_informe(lotes, precios):
    informe = []
    for lote in lotes:
        fruta = lote.nombre
        cajones = lote.cajones
        precio_produccion = lote.precio
        cambio = precios[fruta] - precio_produccion
        informe.append((fruta, cajones, precio_produccion, cambio))
    return informe
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