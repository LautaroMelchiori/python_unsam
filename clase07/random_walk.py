import numpy as np
import matplotlib.pyplot as plt

# Ejercicio 7.10

# 3)
# Colocamos una semilla para permitir reproducibilidad entre corridas
np.random.seed(2)

def randomwalk(largo):
    pasos=np.random.randint (-1, 2, largo)    
    return pasos.cumsum()

def max_valor_absoluto(array):
    """
    Recibe un array y devuelve el maximo valor absoluto entre sus elementos
    """
    maximo = np.amax(array)
    minimo = np.absolute(np.amin(array))
    return maximo if maximo > minimo else minimo

N = 100000

fig = plt.figure(figsize = (12.8 / 2.54, 9.6 / 2.54))

plt.subplot2grid((2, 2), (0, 0), colspan = 2)
plt.ylim(-1000, 1000)
plt.yticks((-500, 0, 500))
plt.xticks([])
plt.title("12 Caminatas al azar")

# acortamos el llamado a la funcion np.random.random()
rand = lambda: np.random.random()

# registro de las caminatas junto al punto mas alejado del origen al que llegaron
random_walks = {}
for _ in range(12):
    random_walk = randomwalk(N)

    # la clave es el maximo valor absoluto (que sera el punto que mas se aleje del origen)
    # y el valor sera la caminata en cuestion
    random_walks[max_valor_absoluto(random_walk)] = random_walk

    # ploteamos la caminata usando 3 valores aleatorios para RGB
    # obteniendo un color aleatorio para cada caminata
    plt.plot(random_walk, color = (rand(), rand(), rand()))

distancias_al_origen = list(random_walks.keys())
mayor_dist = max(distancias_al_origen)
menor_dist = min(distancias_al_origen)

plt.subplot(2, 2, 3)
plt.plot(random_walks[mayor_dist])
plt.ylim(-1000, 1000)
plt.yticks((-500, 0, 500))
plt.xticks([])
plt.title("La caminata que más se aleja")

plt.subplot(2, 2, 4)
plt.plot(random_walks[menor_dist])
plt.ylim(-1000, 1000)
plt.yticks([])
plt.xticks([])
plt.title("La caminata que menos se aleja")

plt.show()

"""
1)

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

N = 100000

plt.xlabel('Tiempo')
plt.ylabel('Distancia al origen')
plt.title('Caminata al azar')

plt.plot(randomwalk(N))
plt.show()

2) 

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

N = 100000

# acortamos el llamdo a la funcion np.random.random()
rand = lambda: np.random.random()
for _ in range(12):
    # usamos 3 valores aleatorios para RGB
    plt.plot(randomwalk(N), color = (rand(), rand(), rand()))


plt.xlabel('Tiempo')
plt.ylabel('Distancia al origen')
plt.title('Caminata al azar')

plt.show()
"""