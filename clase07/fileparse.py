# fileparse.py
import csv

"""
# Ejercicio 6.6

def parse_csv(nombre_archivo):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)

        # Lee los encabezados
        headers = next(rows)
        registros = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            registro = dict(zip(headers, row))
            registros.append(registro)

    return registros

# Ejercicio 6.7

def parse_csv(nombre_archivo, select = None):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        encabezados = next(filas)

        # Si se indicó un selector de columnas,
        # buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]

            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros

# Ejercicio 6.8

def parse_csv(nombre_archivo, select = None, types = None):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    Se puede elegir el tipo de dato en que cada fila debe ser devuelta, determinando el parámetro types, que debe ser una lista de funciones de conversión (str, float, int, etc.)
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        encabezados = next(filas)

        # Si se indicó un selector de columnas,
        # buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]

            # Convertir tipos de datos si se especificaron
            if types:
                fila = [func(val) for func, val in zip(types, fila) ]
            
            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros
"""
# Ejercicio 6.9
# Lancemos errores, Atrapemos errores y ejercicio 7.1 agregados

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True, silence_errors = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    Se puede elegir el tipo de dato en que cada fila debe ser devuelta, determinando el parámetro types, que debe ser una lista de funciones de conversión (str, float, int, etc.).
    Se puede parsear un archivo sin encabezados, determinando el parametro has_headers a False, en cuyo caso la funcion devolvera una lista de tuplas, una por fila
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Si hay encabezados en el archivo, los lee
        if has_headers:
            encabezados = next(filas)

            # Si se indicó un selector de columnas,
            # buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios

            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []

            registros = []
            for index, fila in enumerate(filas):
                if not fila:    # Saltear filas vacías
                    continue

                try:
                    # Filtrar la fila si se especificaron columnas
                    if indices:
                        fila = [fila[index] for index in indices]

                    # Convertir tipos de datos si se especificaron
                    if types:
                        fila = [func(val) for func, val in zip(types, fila)]
                    
                    # Armar el diccionario y agregarlo a la lista
                    registro = dict(zip(encabezados, fila))
                    registros.append(registro)
                # Manejamos el error que puede surgir en caso que no podamos procesar cierta fila
                except ValueError as error:
                    if not silence_errors:
                        print(f'Fila {index + 1}: No pude convertir {fila}')
                        print(f'Fila {index + 1}: Motivo: {error}')
                
        # Si no hay encabezados, devolveremos una lista de tuplas representando la informacion de las filas
        else:
            # Si se nos pide seleccionar encabezados, pero no los hay, lanzamos un error
            if select is not None:
                raise RuntimeError("Para seleccionar, necesito encabezados.")
            
            registros = []
            for index, fila in enumerate(filas):
                if not fila: # Saltear filas vacías
                    continue
                
                try:
                    # Convertir tipos de datos si se especificaron
                    if types:
                        fila = [func(val) for func, val in zip(types, fila)]

                    # Armar la tupla y agregarla a la lista
                    registro = tuple(fila)
                    registros.append(registro)
                # Manejamos el error que puede surgir en caso que no podamos procesar cierta fila
                except ValueError as error:
                    if not silence_errors:
                        print(f'Fila {index + 1}: No pude convertir {fila}')
                        print(f'Fila {index + 1}: Motivo: {error}')
                    
    return registros