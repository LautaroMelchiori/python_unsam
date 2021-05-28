# ejercicio 11.9

def pascal(n, k):
    """
    Recibe dos coordenadasn n y k, ambas >= 0

    Devuelve el numero ubicado en esa posicion
    en un triangulo de pascal
    """

    if n == 0:
        if k == 0:
            return 1
        else:
            return 0
    
    return pascal(n - 1, k - 1) + pascal(n - 1, k)

# imprime un triangulo de pascal con 5 filas
n = 5
for i in range(n):
    print(" " * (n - i), end = '')
    for j in range(i+1):
        print(f'{pascal(i, j)} ', end='')
    print()