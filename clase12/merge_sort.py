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
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
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
