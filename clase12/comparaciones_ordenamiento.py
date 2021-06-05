# ejercicio 12.5
# Modificado ejercicio 12.7

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# semilla para fijar reproducibilidad
np.random.seed(250)

#from burbujeo import ord_burbujeo
#from ord_insercion import ord_insercion
#from ord_seleccion import ord_seleccion
#from merge_sort import merge_sort


# Agrego el codigo de todos los metodos
# para tener todo junto en el archivo a entregar


def merge_sort(lista, comps=0):
    """
    Ordena lista mediante el método merge sort.

    Pre: lista debe contener elementos comparables.

    Devuelve: un diccionario con la lista ordenada y
    la cantidad de comparaciones hechas para ordenarla
    """
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2

        izq = merge_sort(lista[:medio])
        lista_izq = izq['lista']

        der = merge_sort(lista[medio:])
        lista_der = der['lista']

        res_merge = merge(lista_izq, lista_der)

        lista_nueva = res_merge['lista']

        comps += res_merge['comps'] + der['comps'] + izq['comps']

    return {'lista': lista_nueva, 'comps': comps}


def merge(lista1, lista2):
    """
    Intercala los elementos de lista1 y lista2 de forma ordenada.

    Pre: lista1 y lista2 deben estar ordenadas.

    Devuelve: devuelve un diccionario con una 
    lista con los elementos de lista1 y lista2
    y la cantidad de comparaciones realizadas
    """
    i, j = 0, 0
    resultado = []
    comps = 0

    while(i < len(lista1) and j < len(lista2)):
        comps += 1
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return {'lista': resultado, 'comps': comps}


def ord_insercion(lista):
    """
    Ordena una lista de elementos según el método de inserción.

    Pre: los elementos de la lista deben ser comparables.
    Post: la lista está ordenada.
    """

    comparaciones = 0

    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            comparaciones += reubicar(lista, i + 1)
        #print("DEBUG: ", lista)

    return comparaciones


def reubicar(lista, p):
    """
    Reubica al elemento que está en la posición p de la lista
    dentro del segmento [0:p-1].

    Pre: p tiene que ser una posicion válida de lista.
    """

    comparaciones = 0

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        comparaciones += 1
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v

    return comparaciones + 1


def ord_burbujeo(lista):
    """
    Ordena una lista de elementos según el método de burbujeo.
    Pre: los elementos de la lista deben ser comparables.
    Post: la lista está ordenada.
    """
    comparaciones = 0
    for i in range(1, len(lista)):
        for j in range(len(lista) - i):
            comparaciones += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return comparaciones


def ord_seleccion(lista):
    """
    Ordena una lista de elementos según el método de selección.

    Pre: los elementos de la lista deben ser comparables.
    Post: la lista está ordenada.
    """

    comparaciones = 0

    # posición final del segmento a tratar
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)
        comparaciones += n

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        #print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1

    return comparaciones


def buscar_max(lista, a, b):
    """
    Devuelve la posición del máximo elemento en un segmento de
    lista de elementos comparables.

    La lista no debe ser vacía.
    a y b son las posiciones inicial y final del segmento
    """

    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max


def generar_lista(N):
    """
    Genera una lista de largo N, 
    poblado con numeros enteros
    pseudo-aleatorios del 1-1000
    """
    return [np.random.randint(1, 1001) for _ in range(N)]


k = 500

comparaciones_seleccion = []
comparaciones_insercion = []
comparaciones_burbujeo = []
comparaciones_merge = []

N = []
for n in range(1, k + 1):
    N.append(n)
    lista = generar_lista(n)
    comparaciones_seleccion.append(ord_seleccion(lista.copy()))
    comparaciones_insercion.append(ord_insercion(lista.copy()))
    comparaciones_burbujeo.append(ord_burbujeo(lista.copy()))
    comparaciones_merge.append(merge_sort(lista.copy())['comps'])

# convertimos la lista de las comparaciones de insercion a una serie
# de pandas y usamos la media movil para suavizar los datos
serie = pd.Series(comparaciones_insercion)
comparaciones_insercion = serie.rolling(30, min_periods=1).mean()

plt.plot(N, comparaciones_seleccion, color='red', label='Seleccion')
plt.plot(N, comparaciones_insercion, label='Insercion')
plt.plot(N, comparaciones_burbujeo, linestyle='--',
         color='blue', label='Burbujeo')
plt.plot(N, comparaciones_merge, label='Merge')

plt.xlabel('Longitud de la lista a ordenar')
plt.ylabel('Cantidad de operaciones realizadas')
plt.legend()

plt.savefig('Comparaciones.png')

plt.show()
