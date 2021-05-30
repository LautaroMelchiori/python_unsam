# ejercicio 11.10

def combinaciones(lista, n):
    """
    Recibe una lista de caracteres unicos, 
    y un numero k, e imprime todas las posibles
    cadenas de longitud k formadas con los caracteres dados 
    (permitiendo caracteres repetidos).

    Ejemplo: combinaciones(['a', 'b', 'c'], 2) -> aa ab ac ba bb bc ca cb cc
    """

    if n == 1:
        return lista

    lista_combinaciones = []

    for i in lista:
        for j in combinaciones(lista, n - 1):
            lista_combinaciones.append(i + j)
    
    return lista_combinaciones