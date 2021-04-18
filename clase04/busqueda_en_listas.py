def buscar_u_elemento(lista, elem):
    # Busca y devuelve el indice de la ultima aparicion del elemento dado en la lista, o -1 si no esta
    ultimo_elemento = -1  # arrancamos suponiendo que el elemento no esta en la lista
    for indice, elemento in enumerate(lista):
        # Si encontramos una coincidencia en la lista, esa sera la ultima aparicion del elemento
        if elemento == elem:
            ultimo_elemento = indice 
        
    return ultimo_elemento

# input:  buscar_u_elemento([1,2,3,2,3,4],1)
# output: 0

def buscar_n_elemento(lista, elem):
    # Cuenta la cantidad de apariciones de un elemento en una lista
    cantidad_de_apariciones = 0
    for elemento in lista:
        if elemento == elem:
            cantidad_de_apariciones += 1

    return cantidad_de_apariciones

# input: buscar_n_elemento([1, 1, 2, 1], 1)
# output: 3

def maximo(lista):
    # Devuelve el máximo de una lista,  la lista debe ser no vacía
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = lista[0] # Inicializamos m como el primer elemento de la lista
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e

    return m

# input: maximo([1,2,7,2,3,4])
# output: 7

def minimo(lista):
    # Devuelve el mínimo de una lista, la cual debe no estar vacía
    minimo = lista[0] # Inicializamos minimo como el primer elemento de la lista
    for elemento in lista:
        # si encontramos un elemento que es menor que el actual minimo, actualizamos
        if elemento < minimo:
            minimo = elemento

    return minimo

# input: minimo([1, 2, 0, 0.5, -1])
# output: -1