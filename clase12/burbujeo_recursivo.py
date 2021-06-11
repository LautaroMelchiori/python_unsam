def ord_burbujeo(lista, idx=1, comps=0):
    """
    Recibe una lista y la ordena
    """
    if idx == len(lista):
        return lista, comps

    for j in range(len(lista) - idx):
        comps += 1
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return ord_burbujeo(lista, idx + 1, comps)
