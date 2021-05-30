# ejercicio 11.8

def replicar(lista, n):
    """
    Replica los elementos de lista, n veces

    Devuelve la lista resultante de la siguiente manera:
    replicar([1, 3, 3, 7], 2) -> ([1, 1, 3, 3, 3, 3, 7, 7])
    """

    def replicar_aux(lista, n, lista_modif, idx = 0):
        if len(lista_modif) == len(lista) * n:
            return lista_modif
        
        for _ in range(n):
            lista_modif.append(lista[idx])
        
        return replicar_aux(lista, n, lista_modif, idx + 1)

    return replicar_aux(lista, n, [])