import random as r

#---------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 5.1

def tirar():
    return [r.randint(1,6) for _ in range(5)]

def es_generala(tirada):
    generala = tirada[0]
    for i in range(1, 5):
        if tirada[i] == generala:
            continue
        else:
            return False

    return True

N = 1000000
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

# Los resultados varian menos con N = 1.000.000 ya que a mayor numero de experimentos mayor precision de la estimacion

# Realice el experimento con N = 30.000.000 y me salieron 23.196 generalas servidas
# por lo que podemos concluir que, en promedio, una generala servida sale cada 1293 tiradas

# La probabilidad puede calcularse de manera exacta tomando uno de los dados y calculando la probabilidad de que el resto sean iguales a este
# La probabilidad de que un dado salga con un numero determinado es de 1/6, 
# asi que la probabilidad de que los otros 4 dados salgan iguales al primero es de (1/6) * 4, 
# o sea, la probabilidad de una generala servida es de 1/1296

# La estimacion con 30.000.000 de tiradas se acerco bastante a la probabilidad exacta, 
# y si aumentasemos el numero de experimentos se acercaria aun mas

#---------------------------------------------------------------------------------------------------------------------------------------------