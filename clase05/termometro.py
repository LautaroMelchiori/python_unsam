import random
import numpy as np

# Ejercicio 5.5

MU = 0
SIGMA = 0.2
n = 999
temp = 37.5
mediciones = np.empty(n)

# simulamos n mediciones calculando el margen de error
for i in range(n):
    error = random.normalvariate(MU, SIGMA)
    
    medicion = temp + error
    
    mediciones[i] = medicion

    print(f'{i+1}: {medicion:.6f}')

mediciones.sort()
max_medicion = max(mediciones)
min_medicion = min(mediciones)
prom_medicion = sum(mediciones) / n
mediana = mediciones[int((n / 2) - 0.5)]

# restamos uno al calcular cuartiles para compensar el hecho de que los indices de las listas arrancan en 0 y no en 1
primer_cuartil = mediciones[int((n+1)/4) - 1]
segundo_cuartil = mediana
tercer_cuartil = mediciones[int((3*(n+1))/4) - 1]

print()
print(f'Maxima medicion: {max_medicion:.6f}')
print(f'Minima medicion: {min_medicion:.6f}')
print(f'Medicion promedio: {prom_medicion:.6f}')
print(f'Mediana: {mediana:.6f}')
print()
print(f'Primer cuartil: {primer_cuartil:.6f}')
print(f'Segundo cuartil: {segundo_cuartil:.6f}')
print(f'Tercer cuartil: {tercer_cuartil:.6f}')

# Ejercicio 5.7

np.save("../Data/Temperaturas.npy", mediciones)