# ejercicio 11.7

def maximo(lista):
    """
    Recibe una lista

    Devuelve el mayor elemento de la misma
    """
    if len(lista) == 1:
        return lista[0]

    max_resto = maximo(lista[1:])

    return max_resto if max_resto > lista[0] else lista[0]