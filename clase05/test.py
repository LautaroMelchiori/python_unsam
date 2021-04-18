import time
import random
from itertools import groupby
import matplotlib.pyplot as plt
import numpy as np

def tirar():
    return [random.randint(1,6) for _ in range(5)]

x = np.load("../Data/Temperaturas.npy")
print(x)
N = 3000000
#sumas = [sum(tirar()) for i in range(N)]
#plt.hist(sumas, bins = 26, density = True)
#plt.show()
# def propagar_lauty(lista):
#     hay_fuego = False
#     propagado = list(lista)
#     a_prender = []
#     for i, f in enumerate(lista):
#         if f == 0:
#             if hay_fuego:
#                 propagado[i] = 1
#             else:
#                 a_prender.append(i)
#         elif f == 1:
#             hay_fuego = True
#             for i in a_prender:
#                 propagado[i] = 1
#         else:
#             hay_fuego = False
#             a_prender = []
#     return propagado

# def inv_lista_1(lista):
#     invertida = []
#     for e in lista:
#         invertida.insert(0, e)
#     return invertida

# def inv_lista_2(lista):
#     invertida = []
#     for e in lista:
#         invertida = [e] + invertida
#     return invertida

# def inv_lista_3(lista):
#     return lista[::-1]

# rang = [i * 0 for i in range(5000000)]
# start = time.time()
# propagar_lauty([1] + rang + [0])
# end = time.time()
# print(end - start)


# def all_equal(iterable):
#     return max(iterable) == min(iterable)


# gens = 0
# count = 1296
# for _ in range(count):
#     tirada = [random.randint(1,6) for _ in range(5)]
#     if all_equal(tirada):
#         gens += 1
# print(gens/count)
# print(1/1296)

