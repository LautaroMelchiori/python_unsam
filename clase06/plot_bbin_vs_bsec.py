import matplotlib.pyplot as plt
import numpy as np
import random

def busqueda_secuencial(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

def busqueda_binaria(lista, x):
    """
    Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    Devuelve tambien la cantidad de comparaciones realizadas
    """
    encontrar_medio = lambda lista: int(len(lista) / 2 - 0.5)
    comps = 0
    medio = encontrar_medio(lista)
    izq = 0
    der = len(lista) - 1

    while lista[izq : der]:
        comps += 1 # sumo las comparaciones que estoy por hacer
        if lista[medio] > x:
            #comps -= 1 # si la primera se cumple, no haremos la segunda comparacion asi que ajustamos el contador
            der = medio - 1
            medio -= encontrar_medio(lista[izq : der + 1]) + 1
        elif lista[medio] < x:
            izq = medio + 1
            medio += encontrar_medio(lista[izq : der + 1]) + 1
        else: # if lista[medio] == x:
            return medio, comps

    comps += 1 # sumo la comparación que estoy por hacer
    if lista[medio] == x:
        return medio, comps
    else:
        return -1, comps

def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0, m-1)

def experimento_secuencial_promedio(lista, m, k):
    """
    Realiza k experimentos y devuelve el promedio de comparaciones realizadas por un algoritmo de busqueda secuencial 
    para encontrar un elemento aleatorio del rango [0 : m) en la lista dada
    """
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

def experimento_binario_promedio(lista, m, k):
    """
    Realiza k experimentos y devuelve el promedio de comparaciones realizadas por un algoritmo de busqueda binaria
    para encontrar un elemento aleatorio del rango [0 : m) en la lista dada
    """
    comps_tot = 0
    for _ in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista, x)[1]

    comps_prom = comps_tot / k
    return comps_prom

m = 100000
k = 1000

# estos son los largos de listas que voy a usar
largos = np.arange(256) + 1 

# aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
comps_promedio_secuencial = np.zeros(256) 
comps_promedio_binaria = np.zeros(256)

for i, n in enumerate(largos):
    lista = generar_lista(n, m) # genero lista de largo n
    comps_promedio_secuencial[i] = experimento_secuencial_promedio(lista, m, k)
    comps_promedio_binaria[i] = experimento_binario_promedio(lista, m, k)

# ahora grafico largos de listas contra operaciones promedio de búsqueda.
plt.plot(largos, comps_promedio_secuencial, label = 'Búsqueda Secuencial')
plt.plot(largos, comps_promedio_binaria, label = 'Búsqueda Binaria')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaciones")
plt.title("Complejidad de la Búsqueda")
plt.legend()
plt.show()