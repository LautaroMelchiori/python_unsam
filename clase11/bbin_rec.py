# ejercicio 11.11

def bbinaria_rec(lista, e):
    if len(lista) == 0:
        return False
    elif len(lista) == 1:
        return lista[0] == e
    else:
        medio = len(lista)//2

    if lista[medio] == e:
        return True
    elif lista[medio] > e:
        return bbinaria_rec(lista[:medio], e)
    else:
        return bbinaria_rec(lista[medio + 1:], e)