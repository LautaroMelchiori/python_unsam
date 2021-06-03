def ord_burbujeo(lista, idx = 1):
    """
    Recibe una lista y la ordena
    """
    if idx == len(lista):
        return lista

    for j in range(len(lista) - idx):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    ord_burbujeo(lista, idx + 1)