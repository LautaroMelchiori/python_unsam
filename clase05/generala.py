import random as r
from collections import Counter
import time

# Ejercicio 5.2

def tirar(n_dados):
    return [r.randint(1,6) for _ in range(n_dados)]

def analizar_tirada(tirada):
    "retorna una tupla con el numero mas repetido y la cantidad de dados con este"
    iguales = Counter()
    for dado in tirada:
        iguales[dado] += 1
    return iguales.most_common(1)[0]

def jugar():
    # Retorna True si logra sacar generala usando 3 tiros, de lo contrario False
    # Esta version de jugar se queda con un dado aleatorio y tira el resto si salen todos distintos
    tirada = tirar(5)
    for _ in range(3):
        numero_mas_repetido, numero_de_repeticiones = analizar_tirada(tirada)
        # Si obtenemos generala, retorna True
        if numero_de_repeticiones == 5:
            return True
        else:
            # Si no hay generala, generamos una nueva tirada quedandonos con los dados que nos sirven y volviendo a tirar el resto
            tirada = [numero_mas_repetido] * numero_de_repeticiones + tirar(5 - numero_de_repeticiones)
    return False

# Extra

def jugar_extra():
    # Retorna True si logra sacar generala usando 3 tiros, de lo contrario False
    # Esta version de jugar() vuelve a tirar todos los dados si salen todos distintos
    tirada = tirar(5)
    for _ in range(3):
        numero_mas_repetido, numero_de_repeticiones = analizar_tirada(tirada)
        # Si obtenemos generala, retorna True
        if numero_de_repeticiones == 5:
            return True
        # Si el numero con mas apariciones es 1 significa que todos los dados son distintos, por lo cual volveriamos a tirar todos de nuevo
        elif numero_de_repeticiones == 1:
            tirada = tirar(5)
        else:
            # Si no hay generala, generamos una nueva tirada quedandonos con los dados que nos sirven y volviendo a tirar el resto
            tirada = [numero_mas_repetido] * numero_de_repeticiones + tirar(5 - numero_de_repeticiones)
    return False


N = 10000
G1 = sum([jugar() for _ in range(N)])
G2 = sum([jugar_extra() for _ in range(N)])
prob1 = G1/N
prob2 = G2/N
print('Estrategia quedarte uno y tirar el resto si salen todos distintos:')
print(f'Tiré {N} veces, de las cuales {G1} saqué generala.')
print(f'Podemos estimar la probabilidad de sacar generala mediante {prob1:.6f}.')
print()
print('Estrategia tirar todos de nuevo si salen todos distintos:')
print(f'Tiré {N} veces, de las cuales {G2} saqué generala.')
print(f'Podemos estimar la probabilidad de sacar generala mediante {prob2:.6f}.')
print()
print('Viendo que las probabilidades con las dos estrategias son muy similares, podemos concluir que ninguna de las dos es mejor que la otra')