# ejercicio 12.8
# ejercicio 12.9

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import timeit as tt

np.random.seed(30)


def ord_merge(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = ord_merge(lista[:medio])
        der = ord_merge(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva


def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado


def ord_merge3sort(lista):
    if len(lista) < 2:
        lista_nueva = lista
    elif len(lista) == 2:
        return lista if lista[0] <= lista[1] else lista[::-1]
    else:
        primer_corte = len(lista) // 3
        segundo_corte = primer_corte * 2

        primer_tercio = ord_merge3sort(lista[:primer_corte])
        segundo_tercio = ord_merge3sort(lista[primer_corte:segundo_corte])
        tercer_tercio = ord_merge3sort(lista[segundo_corte:])

        lista_nueva = merge3sort(primer_tercio, segundo_tercio, tercer_tercio)

    return lista_nueva


def merge3sort(lista1, lista2, lista3):
    merge_primeras2 = merge(lista1, lista2)
    merge_total = merge(merge_primeras2, lista3)

    return merge_total


def ord_insercion(lista):
    """
    Ordena una lista de elementos según el método de inserción.

    Pre: los elementos de la lista deben ser comparables.
    Post: la lista está ordenada.
    """

    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
        #print("DEBUG: ", lista)


def reubicar(lista, p):
    """
    Reubica al elemento que está en la posición p de la lista
    dentro del segmento [0:p-1].

    Pre: p tiene que ser una posicion válida de lista.
    """

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v


def ord_burbujeo(lista):
    """
    Ordena una lista de elementos según el método de burbujeo.
    Pre: los elementos de la lista deben ser comparables.
    Post: la lista está ordenada.
    """
    for i in range(1, len(lista)):
        for j in range(len(lista) - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


def ord_seleccion(lista):
    """
    Ordena una lista de elementos según el método de selección.

    Pre: los elementos de la lista deben ser comparables.
    Post: la lista está ordenada.
    """

    # posición final del segmento a tratar
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        #print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1


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


def generar_listas(Nmax):
    listas = []
    for N in range(1, Nmax):
        listas.append(generar_lista(N))

    return listas


def experimento_timeit(metodo, listas, num):
    """
    Realiza un experimento usando timeit para evaluar el método
    de 'metodo' para ordenamiento de listas
    con las listas pasadas como entrada
    y devuelve los tiempos de ejecución para cada lista
    en un vector.

    El parámetro 'listas' debe ser una lista de listas.

    El parametro 'metodo' debe ser una cadena con un metodo
    Opciones de  metodos: seleccion, merge, burbujeo, insercion, merge3sort

    El parámetro 'num' indica la cantidad de repeticiones a ejecutar el método para cada lista.
    """
    tiempos = []

    global lista

    for lista in listas:

        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo = tt.timeit(
            f'ord_{metodo}(lista.copy())', number=num, globals=globals())

        # guardo el resultado
        tiempos.append(tiempo)

    # paso los tiempos a arrays
    tiempos = np.array(tiempos)

    return tiempos


listas = generar_listas(500)

metodos = ['seleccion', 'insercion', 'burbujeo', 'merge', 'merge3sort']
tiempos = {}

for metodo in metodos:
    tiempos[metodo] = experimento_timeit(metodo, listas, 1)

    tiempos[metodo] = pd.Series(tiempos[metodo])
    tiempos[metodo] = tiempos[metodo].rolling(50, min_periods=1).mean()

    plt.plot(tiempos[metodo], label=metodo)


plt.xlabel('Longitud de la lista a ordenar')
plt.ylabel('Tiempo tardado (segundos)')

# plt.savefig('Comparaciones_temporales.png')

plt.legend()
plt.show()
