import numpy as np
import random
import matplotlib.pyplot as plt

# Ejercicio 5.9
def crear_album(figus_total):
    return np.zeros(figus_total)

# Ejercicio 5.10
def album_incompleto(A):
    return 0 in A

# Ejercicio 5.11 
def comprar_figu(figus_total):
    return random.randint(0, figus_total - 1)

# Ejercicio 5.12
def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    figus_compradas = 0
    while album_incompleto(album):
        album[comprar_figu(figus_total)] = 1
        figus_compradas += 1

    return figus_compradas

# Ejercicio 5.13 y 5.14
def calcular_promedio_figus(figus_total, n_repeticiones):
    # calcula un promedio de figus que es necesario comprar para completar el album
    # figus_total es el tamaño del album a completar y n_repeticiones la cantidad de simulaciones que queremos realizar para sacar el promedio
    albums_completados = [cuantas_figus(figus_total) for _ in range(n_repeticiones)]
    promedio_figus = np.mean(albums_completados)
    return promedio_figus

print(f'Hay que comprar, en promedio, {calcular_promedio_figus(6, 1000)} figus para completar un album de 6')

print(f'Hay que comprar, en promedio, {calcular_promedio_figus(670, 100)} figus para completar un album de 670')

# Ejercicio 5.15 y 5.16
def comprar_paquete(figus_total, figus_paquete, con_figus_repetidas):
    if con_figus_repetidas:
        return [comprar_figu(figus_total) for _ in range(figus_paquete)]
    else:
        # si queremos un paquete SIN figus repetidas, usamos random.sample() en vez de random.randint() para tener valores unicos en el paquete
        return random.sample(range(figus_total), k = figus_paquete)
        

# Ejercicio 5.17
def cuantos_paquetes(figus_total, figus_paquete, paquetes_con_figus_repetidas):
    # paquetes_con_figus_repetidas es un booleano que indica si queremos calcular con paquetes que pueden tener figus repetidas o no
    album = crear_album(figus_total)
    paquetes = 0
    while album_incompleto(album):
        for figu in comprar_paquete(figus_total, figus_paquete, paquetes_con_figus_repetidas):
            album[figu] = 1
        paquetes += 1
    return paquetes

# Ejercicio 5.18
def calcular_promedio_paquetes(figus_total, figus_paquete, n_repeticiones):
    # calcula un promedio de figus que es necesario comprar para completar el album
    # figus_total es el tamaño del album a completar y n_repeticiones la cantidad de simulaciones que queremos realizar para sacar el promedio
    albums_completados = [cuantos_paquetes(figus_total, figus_paquete, True) for _ in range(n_repeticiones)]
    promedio_paquetes = np.mean(albums_completados)
    return promedio_paquetes

promedio_paquetes_solo = calcular_promedio_paquetes(670, 5, 100)
print(f'Hay que comprar, en promedio, {promedio_paquetes_solo} paquetes para completar un album de 670 figus')

# GRAFICO DEL LLENADO DEL ALBUM

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete, True)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5

plt.figure()
plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")

# Ejercicio 5.19
def calcular_probabilidad(n_figus, n_paquetes, n_figus_paquete):
    # estima la probabilidad de completar un album de n_figus con n_paquetes con n_figus_paquete cada uno
    N = 1000
    simulaciones = [cuantos_paquetes(n_figus, n_figus_paquete, True) for _ in range(N)]

    # casos_favorables = sum([1 for x in simulaciones if x <= n_paquetes])

    # Usando ndarrays
    n_paquetes_hasta_llenar = np.array(simulaciones)
    casos_favorables = (n_paquetes_hasta_llenar <= n_paquetes).sum()

    return casos_favorables / N

print()
print(f'Estimo la probabilidad de completar el album con 850 paquetes o menos en {calcular_probabilidad(670, 850, 5) * 100}%')

# Ejercicio 5.20
paquetes = np.array([cuantos_paquetes(670, 5, True) for _ in range(1000)])

plt.figure()
plt.xlabel("Cantidad de paquetes comprados")
plt.ylabel("Cantidad de simulaciones favorables")
plt.title("Promedio de paquetes necesarios para completar album")
plt.hist(paquetes, bins = 50)

plt.show()

# Ejercicio 5.21
# Para estimar la cantidad de paquetes necesarios para tener 90% de chances de completar el album generamos N simulaciones, 
# y guardamos en una lista la cantidad de paquetes que nos tomo completar el album en cada simulacion
# La cantidad de paquetes que se encuentre en el indice N * 0.9 nos dara APROXIMADAMENTE un 90% de chances de completar album
# Si quisieramos buscar la cantidad de paquetes para tener 70% de chances buscariamos en el indice N * 0.7
N = 1000
indice_90_porciento = int(N * 0.9)

simulaciones_con_repes = [cuantos_paquetes(670, 5, True) for _ in range(N)]
simulaciones_con_repes.sort()
num_estimado_con_repes = simulaciones_con_repes[indice_90_porciento]

# Ejercicio 5.22
simulaciones_sin_repes = [cuantos_paquetes(670, 5, False) for _ in range(N)]
simulaciones_sin_repes.sort()
num_estimado_sin_repes = simulaciones_sin_repes[indice_90_porciento]

print()
print(f'Para tener un 90% de chance de completar el album comprando paquetes CON figus repetidas, necesitamos aproximadamente {num_estimado_con_repes}')
print(f'Para tener un 90% de chance de completar el album comprando paquetes SIN figus repetidas, necesitamos aproximadamente {num_estimado_sin_repes}')
print(f'El numero de paquetes cambia muy poco ya que al sacar 5 muestras de una una pileta de 670 elementos la probabilidad de sacar repetidas en un mismo paquete ya es de por si muy baja')

# Ejercicio 5.23
def completar_con_amigos(figus_total, figus_paquete, paquetes_con_figus_repetidas, n_amigos):
    # paquetes_con_figus_repetidas es un booleano que indica si queremos calcular con paquetes que pueden tener figus repetidas o no

    # Para llenar los albumes de todos nuestros amigos necesitamos tener n_amigos cantidad de figuritas de cada una

    # Lo que hice fue usar una sola estructura de datos para almacenar las figus que tengo,
    # y cuando tenga n_amigos cantidad de figus (o mas) de cada una, significa que tenemos suficientes para llenar todos los albumes

    stock_de_figus = np.zeros(figus_total)
    paquetes = 0

    while (stock_de_figus < n_amigos).sum() != 0:
        for figu in comprar_paquete(figus_total, figus_paquete, paquetes_con_figus_repetidas):
            stock_de_figus[figu] += 1
        paquetes += 1
    return paquetes

n_simulaciones = 100
n_amigos = 5
simulaciones_con_amigos = [completar_con_amigos(figus_total, figus_paquete, True, n_amigos) for _ in range(n_simulaciones)]
promedio_completar_con_amigos = np.mean(simulaciones_con_amigos)

print()
print(f'Hay que comprar, en promedio, {promedio_completar_con_amigos} paquetes para completar nuestros albumes de 670 figus con {n_amigos} amigos')
print(f'Esto nos da un promedio de {promedio_completar_con_amigos / n_amigos} paquetes por persona, mientras que para completar el album solo una persona necesitaria, aproximadamente, {promedio_paquetes_solo}')