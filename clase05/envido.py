import random
from collections import Counter

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'basto', 'copa', 'espada']

mazo = [(valor, palo) for valor in valores for palo in palos]

def analizar_envido(mano):
    # Toma una mano y devuelve el envido si es que hay, False de lo contrario

    # Para tener envido necesitamos un palo repetido en nuestras cartas,
    # asi que primero checkeamos que tengamos por lo menos 2 cartas del mismo palo
    mismo_palo = Counter()

    for carta in mano:
        mismo_palo[carta[1]] += 1
    
    palo_mas_repetido, apariciones_del_palo = mismo_palo.most_common()[0]

    if apariciones_del_palo == 1:
        return False
    elif apariciones_del_palo == 2:
        # calculamos el envido haciendo 20 + los valores de las cartas cuyo palo sea el palo repetido
        # (notar que no tomamos en cuenta los 10s, 11s y 12s para calcular el envido)
        return 20 + sum([carta[0] for carta in mano if carta[1] == palo_mas_repetido and carta[0] <= 7])
    else:
        valores = []
        for carta in mano:
            if carta[0] <= 7:
                valores.append(carta[0])
            else:
                valores.append(0)
        # si hay 3 cartas del mismo palo, sumamos 20 + las dos mas grandes y obtenemos el envido
        valor_mas_grande = max(valores)
        valores.remove(valor_mas_grande)
        return 20 + valor_mas_grande + max(valores)

N = 1000000
envidos = Counter()
for _ in range(N):
    mano = random.sample(mazo, k = 3)
    envidos[analizar_envido(mano)] += 1

print(f'Repartí {N} manos, y obtuve los siguientes resultados:')
print(f'Envidos de 31: {envidos[31]} => probabilidad de sacar 31: {envidos[31] / N:.6f}')
print(f'Envidos de 32: {envidos[32]} => probabilidad de sacar 32: {envidos[32] / N:.6f}')
print(f'Envidos de 33: {envidos[33]} => probabilidad de sacar 33: {envidos[33] / N:.6f}')
print()
print('''Podemos concluir entonces que las probabilidades (APROXIMADAS) de obtener 32 y 33 son las mismas (las de obtener 32 son en realidad un poco mas bajas), 
mientras que las de obtener 31 se aproximan a ser el doble''')
print('''Esto tiene sentido ya que hay una sola forma de formar un envido de 32 y 33 (7+5 y 7+6, respectivamente)
mientras que hay dos formas de formar un envido de 31 (7+4 y 6+5)''')