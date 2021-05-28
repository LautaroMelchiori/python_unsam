# ejercicio 11.10

def combinaciones(lista, n, idx = 0):
    """
    Recibe una lista de caracteres únicos, 
    y un número k, e imprime todas las posibles
    cadenas de longitud k formadas con los caracteres dados 
    (permitiendo caracteres repetidos).

    Ejemplo: combinaciones(['a', 'b', 'c'], 2) -> aa ab ac ba bb bc ca cb cc
    """

    def aux(lista, n, idx = 0, string = ''):
        if n == len(lista) - 1:
            return ''

        for idx in lista:
            string += lista[idx] + combinaciones(lista[:idx] + lista[idx + 1:], n - 1)

        return string

    print(aux(lista,n))