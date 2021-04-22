# bbin.py

# Funcion de utilidad
def encontrar_medio(lista):
    """
    Devuelve el indice central de una lista
    Si la lista tiene una cantidad par de elementos, devuelve el primer elemento de los dos centrales
    [0, 1, 2, 3] --> devuelve indice 1
    """
    return  int(len(lista) / 2 - 0.5)


# Implementacion propia de una busqueda binaria
def busqueda_binaria(lista, x):
    """
    Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en la lista
    """

    medio = encontrar_medio(lista)
    izq = 0
    der = len(lista) - 1

    while lista[izq : der]:
        if lista[medio] == x:
            return medio
        elif lista[medio] < x:
            izq = medio + 1
            medio += encontrar_medio(lista[izq : der + 1]) + 1
        else:
            der = medio - 1
            medio -= encontrar_medio(lista[izq : der + 1]) + 1

    if lista[medio] == x:
        return medio
    else:
        return -1

# Ejercicio 6.14

def donde_insertar(lista, x):
    """
    Buscar posicion de insercion
    Precondición: la lista está ordenada
    Si x está en la lista devuelve p tal que lista[p] == x, 
    Si x no está en lista devuelve p tal que lista.insert(p, x) inserta x y mantiene la lista ordenada
    """

    medio = encontrar_medio(lista)
    izq = 0
    der = len(lista) - 1

    while lista[izq : der]:
        if lista[medio] == x:
            return medio
        elif lista[medio] < x:
            izq = medio + 1
            medio += encontrar_medio(lista[izq : der + 1]) + 1
        else: # if lista[medio] > x:
            der = medio - 1
            medio -= encontrar_medio(lista[izq : der + 1]) + 1

    if lista[medio] >= x:
        return medio
    else: # if lista[medio] < x:
        return medio + 1

# Ejercicio 6.15

def insertar(lista, x):
    """
    Insertar
    Precondición: la lista está ordenada
    Si x está en la lista Devuelve p tal que lista[p] == x, 
    Si x no está en lista lo inserta en una posición tal que la lista se mantenga ordenada, y devuelve la posición en que inserto
    """

    medio = encontrar_medio(lista)
    izq = 0
    der = len(lista) - 1

    while lista[izq : der]:
        if lista[medio] == x:
            return medio
        elif lista[medio] < x:
            izq = medio + 1
            medio += encontrar_medio(lista[izq : der + 1]) + 1
        else: # if lista[medio] > x:
            der = medio - 1
            medio -= encontrar_medio(lista[izq : der + 1]) + 1

    if lista[medio] == x:
        return medio
    elif lista[medio] > x:
        lista.insert(medio, x)
        return medio
    else: # if lista[medio] < x:
        lista.insert(medio + 1, x)
        return medio + 1