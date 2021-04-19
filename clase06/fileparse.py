# fileparse.py
import csv

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

# Ejercicio 6.9

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
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
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]

                # Convertir tipos de datos si se especificaron
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]
                
                # Armar el diccionario y agregarlo a la lista
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
        # Si no hay encabezados, devolveremos una lista de tuplas representando la informacion de las filas
        else:
            registros = []
            for fila in filas:
                if not fila: # Saltear filas vacías
                    continue
                
                # Convertir tipos de datos si se especificaron
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]

                # Armar la tupla y agregarla a la lista
                registro = tuple(fila)
                registros.append(registro)

    return registros