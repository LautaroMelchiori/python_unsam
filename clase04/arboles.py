import csv
from pprint import pprint

BASE_DE_DATOS = '../Data/arbolado-en-espacios-verdes.csv'

# Ejercicio 4.18

def leer_arboles(nombre_archivo):
    # Dado un archivo esta funcion devuelve una lista de diccionarios con la informacion de cada fila del archivo
    with open(nombre_archivo, 'rt', encoding = 'utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        # Generamos los diccionarios con duos de claves y valores,
        # Para obtener estos duos emparejamos los encabezados de las columnas con los valores correspondientes de la fila actual
        # Repetimos la creacion de un diccionario para cada fila en el archivo
        return [{clave: valor for clave, valor in zip(headers, row)} for row in rows]

arboleda = leer_arboles(BASE_DE_DATOS)

# Ejercicio 4.19
def obtener_alturas(arboleda, especie):
    return [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == especie]

lista_alturas_jacarandas = obtener_alturas(arboleda, 'Jacarandá')

# Ejercicio 4.20

def obtener_alturas_y_diametros(arboleda, especie):
    return [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie]

lista_alturas_y_diametros_jacarandas = obtener_alturas_y_diametros(arboleda, 'Jacarandá')

# Ejercicio 4.21

def medidas_de_especies(especies, arboleda):-
    return {clave: valor for clave, valor in zip(especies, [obtener_alturas_y_diametros(arboleda, especie) for especie in especies])}