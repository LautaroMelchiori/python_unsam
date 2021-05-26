# informe_funciones.py
from camion import Camion
from fileparse import parse_csv
from lote import Lote
import formato_tabla

#--------------------------------------------------------------------------------------------------------------------------
# Ejercicio 2.16
# Modificado ejercicio 6.11
# Modificado ejercicio 7.5
# Modificado ejercicio 9.4
# Modificado ejercicio 10.2

def leer_camion(nombre_archivo):
    """
    Recibe el nombre de un archivo csv conteniendo la data de un camion
    Devuelve una lista de objetos Lote con cada lote del camion
    """
    with open(nombre_archivo, 'rt') as filas:
        lotes = parse_csv(filas, select = ['nombre','cajones','precio'], types = [str, int, float])
        camion = [Lote(lot['nombre'], lot['cajones'], lot['precio']) for lot in lotes]
        return Camion(camion)
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
# Modificado ejercicio 9.5

def imprimir_informe(informe, formateador):
    """
    Recibe un informe y lo imprime en pantalla, formateado como tabla
    """
    formateador.encabezado(['Nombre', 'Cajones', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in informe:
        rowdata = [ nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}' ]
        formateador.fila(rowdata)

def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es .txt
    Alternativas: .csv o .html
    '''
    # Lee archivos de datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Crea la data del informe
    data_informe = hacer_informe(camion, precios)

    # Imprime el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)

# Ejercicio 7.2 y 7.3

def main(parametros):
    if len(parametros) == 4:
        informe_camion(parametros[1], parametros[2], parametros[3])
    elif len(parametros) == 3:
        informe_camion(parametros[1], parametros[2])
    else:
        print('Uso: informe.py archivo_camion archivo_precio formato(opcional)')


if __name__ == '__main__':
    import sys
    main(sys.argv)
#--------------------------------------------------------------------------------------------------------------------------