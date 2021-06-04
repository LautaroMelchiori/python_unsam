# ejercicio 12.5

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from burbujeo import ord_burbujeo
from ord_insercion import ord_insercion
from ord_seleccion import ord_seleccion

def generar_lista(N):
    """
    Genera una lista de largo N, 
    poblado con numeros enteros
    pseudo-aleatorios del 1-1000
    """
    return [np.random.randint(1, 1001) for _ in range(N)]

k = 500

comparaciones_seleccion = []
comparaciones_insercion = []
comparaciones_burbujeo = []
N = []
for n in range(1, k+ 1):
    N.append(n)
    lista = generar_lista(n)
    comparaciones_seleccion.append(ord_seleccion(lista.copy()))
    comparaciones_insercion.append(ord_insercion(lista.copy()))
    comparaciones_burbujeo.append(ord_burbujeo(lista.copy()))

# convertimos la lista a una serie de pandas y usamos la media movil para suavizar los datos
serie = pd.Series(comparaciones_insercion)
comparaciones_insercion = serie.rolling(30, min_periods = 1).mean()

plt.plot(N, comparaciones_seleccion, color = 'red', label = 'Seleccion')
plt.plot(N, comparaciones_insercion, label = 'Insercion')
plt.plot(N, comparaciones_burbujeo, linestyle='--', color = 'blue', label = 'Burbujeo')
plt.legend()
plt.show()