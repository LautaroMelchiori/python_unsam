import csv
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint

BASE_DE_DATOS = '../Data/arbolado-en-espacios-verdes.csv'

# Ejercicio 4.15

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

# Ejercicio 4.16
def obtener_alturas(arboleda, especie):
    return [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == especie]

lista_alturas_jacarandas = obtener_alturas(arboleda, 'Jacarandá')

# Ejercicio 4.17

def obtener_alturas_y_diametros(arboleda, especie):
    return [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie]

lista_alturas_y_diametros_jacarandas = obtener_alturas_y_diametros(arboleda, 'Jacarandá')

# Ejercicio 4.18

def medidas_de_especies(especies, arboleda):
    return {clave: valor for clave, valor in zip(especies, [obtener_alturas_y_diametros(arboleda, especie) for especie in especies])}

# Ejercicio 5.24

def hist_alturas_jacarandas(bins):
    plt.figure()
    plt.xlabel("Altura")
    plt.ylabel("Cantidad de ejemplares")
    plt.title("Alturas de Jacarandas en el arbolado porteño")
    plt.hist(lista_alturas_jacarandas, bins = bins)

hist_alturas_jacarandas(20)

# Ejercicio 5.25

def scatterplot_diametro_alt_jacaranda():
    data = np.array(lista_alturas_y_diametros_jacarandas)
    xs = data[:, 0]
    ys = data[:, 1]
    color = np.random.rand(len(data))

    plt.figure()
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.scatter(xs, ys, s = 50 * (xs/ys), alpha = 0.3, c = color)

scatterplot_diametro_alt_jacaranda()

# Ejercicio 5.26

def scatterplot_de_especies(especies):
    alt_diam_especies = medidas_de_especies(especies, arboleda)
    data = [np.array(alt_diam_especies[especie]) for especie in especies]

    for especie, array in enumerate(data):
        xs = array[:, 0]
        ys = array[:, 1]
        color = np.random.rand(len(array))

        plt.figure()
        plt.xlim(0,30) 
        plt.ylim(0,100)     
        plt.xlabel("diamentro (cm)")
        plt.ylabel("alto (m)")
        plt.title(f"Relacion diametro-alto para {especies[especie]}")
        plt.scatter(xs, ys, s = 50 * (xs/ys), alpha = 0.3, c = color)

scatterplot_de_especies(['Eucalipto', 'Palo borracho rosado', 'Jacarandá'])

# Extra

def scatterplot_de_especies_un_grafico(especies):
    alt_diam_especies = medidas_de_especies(especies, arboleda)
    data = [np.array(alt_diam_especies[especie]) for especie in especies]

    plt.figure()
    plt.xlim(0, 45) 
    plt.ylim(0, 150)     
    plt.xlabel("diamentro (cm)")
    plt.ylabel("alto (m)")

    especies_titulo = ''.join([str(especie) + ', ' for especie in especies[:-1]])
    especies_titulo += f'y {especies[-1]}'

    plt.title(f"Relacion diametro-alto para {especies_titulo}")

    for especie, array in enumerate(data):
        xs = array[:, 0]
        ys = array[:, 1]

        plt.scatter(xs, ys, s = 50 * (xs/ys), alpha = 0.3, label = f'{especies[especie]}')
        plt.legend()

scatterplot_de_especies_un_grafico(['Eucalipto', 'Palo borracho rosado', 'Jacarandá'])

plt.show()