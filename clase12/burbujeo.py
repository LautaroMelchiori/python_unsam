# ejercicio 12.2

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

# La complejidad de este algoritmo es de O(n²),
# ya que mediante los ciclos anidados recorre n veces la lista de longitud n.
