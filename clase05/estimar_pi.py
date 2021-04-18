import random
from math import sqrt

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

def esta_dentro_del_circulo(punto):
    if sqrt(punto[0] ** 2 + punto[1] ** 2) < 1:
        return True
    else:
        return False

N = 100000
M = sum([esta_dentro_del_circulo(generar_punto()) for _ in range(N)])
pi = 4 * (M/N)
print(f'Generando {N} puntos pudimos aproximar el valor de pi a {pi}') 