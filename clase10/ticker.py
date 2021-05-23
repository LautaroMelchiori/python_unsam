# ticker.py
import csv
import sys

import informe
from vigilante import vigilar

# def filtrar_datos(filas, nombres):
#     for fila in filas:
#         if fila['nombre'] in nombres:
#             yield fila

# def cambiar_tipo(rows, types):
#     for row in rows:
#         yield [func(val) for func, val in zip(types, row)]

# def hace_dicts(rows, headers):
#     for row in rows:
#         yield dict(zip(headers, row))

# def elegir_columnas(rows, indices):
#     for row in rows:
#         yield [row[index] for index in indices]

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = ([row[index] for index in [0, 1, 2]] for row in rows)
    rows = ([func(val) for func, val in zip([str, float, int], row)] for row in rows)
    rows = (dict(zip(['nombre', 'precio', 'volumen'], row)) for row in rows)
    return rows

def ticker(camion_file, log_file, fmt):
    """
    Recibe un archivo de camion,
    un archivo al cual trackear para buscar cambios,
    y un formato, que puede ser 'txt', 'csv' o 'html'

    Crea un indicador en tiempo real y con el formato especificado 
    de los nuevos productos que aparezcan en el archivo 'log_file',
    siempre y cuando esos productos esten en el camion 'camion_file'
    """

    camion = informe.leer_camion(camion_file)

    filas = vigilar(log_file)
    filas = parsear_datos(filas)
    filas = (fila for fila in filas if fila['nombre'] in camion)

    # creamos el formateador
    formateador = informe.formato_tabla.crear_formateador(fmt)

    # seteamos el encabezado
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])

    for fila in filas:
        # tomamos la fila actual (que esta en forma de dict)
        # y la convertimos en una lista de cadenas
        fila_actual = [str(fila[i]) for i in fila]

        # formateamos la fila y la imprimimos
        formateador.fila(fila_actual)

if __name__ == '__main__':
    params = sys.argv
    if len(params) == 4:
        ticker(params[1], params[2], params[3])
    else:
        print('Uso: ticker.py "archivo_camion" "archivo log" "formato"')