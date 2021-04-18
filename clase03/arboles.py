# -*- coding: utf-8 -*-

import csv
from collections import Counter
from pprint import pprint

BASE_DE_DATOS = '../Data/arbolado-en-espacios-verdes.csv'

# Ejercicio 3.18

def leer_parque(nombre_archivo, parque):
    arboles = []
    breakpoint()
    with open(nombre_archivo, 'rt', encoding="utf-8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            arbol = dict(zip(headers, row))
            if arbol['espacio_ve'] == parque:
                arboles.append(arbol)
    return arboles


LISTA_ARBOLES_GRAL_PAZ = leer_parque(BASE_DE_DATOS, 'GENERAL PAZ')
LISTA_ARBOLES_ANDES = leer_parque(BASE_DE_DATOS, 'ANDES, LOS')
LISTA_ARBOLES_CENTENARIO = leer_parque(BASE_DE_DATOS, 'CENTENARIO')

# Ejercicio 3.19

def especies(lista_arboles):
    especies = set()
    for arbol in lista_arboles:
        especies.add(arbol['nombre_com'])
    return especies

# Ejercicio 3.20

def contar_ejemplares(lista_arboles):
    contador_ejemplares = Counter()
    for arbol in lista_arboles:
        contador_ejemplares[arbol['nombre_com']] += 1
    return contador_ejemplares

especies_mas_comunes_gral_paz = contar_ejemplares(LISTA_ARBOLES_GRAL_PAZ).most_common(5)
especies_mas_comunes_los_andes = contar_ejemplares(LISTA_ARBOLES_ANDES).most_common(5)
especies_mas_comunes_centenario = contar_ejemplares(LISTA_ARBOLES_CENTENARIO).most_common(5)

# Apareamos las 5 especies mas comunes de cada parque, asi tendremos filas para nuestra tabla
especies_mas_comunes_apareadas = zip(especies_mas_comunes_gral_paz, especies_mas_comunes_los_andes, especies_mas_comunes_centenario)

print('Tabla mostrando las 5 especies mas comunes de varios parques')
print('----------------------------------------------------------------------------')
# Encabezado de la tabla con los nombres de los parques
print(f"{'General Paz':<25s} {'Los Andes':<25s} {'Centenario':<25s}")
for especie_gral_paz, especie_andes, especie_centenario in especies_mas_comunes_apareadas:
    # Armamos el elemento para cada celda de la tabla con el nombre de la especie y el numero de ejemplares
    especie_gral_paz_con_numero = f'{especie_gral_paz[0]}: {especie_gral_paz[1]}'
    especie_andes_con_numero = f'{especie_andes[0]}: {especie_andes[1]}'
    especie_centenario_con_numero = f'{especie_centenario[0]}: {especie_centenario[1]}'
    print('----------------------------------------------------------------------------')
    # Imprimimos en orden la especie de cada parque, formando una fila de la tabla
    print(f"{especie_gral_paz_con_numero:<25s} {especie_andes_con_numero:<25s} {especie_centenario_con_numero:<25s}")
print('----------------------------------------------------------------------------')
print()

# Ejercicio 3.21

def obtener_alturas(lista_arboles, especie):
    alturas = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            alturas.append(float(arbol['altura_tot']))
    return alturas


# Dada una especie, genera una tabla con los resultados de altura en tres parques
def imprimir_tabla_alturas(especie):
    lista_gral_paz = obtener_alturas(LISTA_ARBOLES_GRAL_PAZ, especie)
    lista_andes = obtener_alturas(LISTA_ARBOLES_ANDES, especie)
    lista_centenario = obtener_alturas(LISTA_ARBOLES_CENTENARIO, especie)
    print(f'Tabla mostrando los resultados de alturas de {especie} en tres parques')
    print('----------------------------------------------------------------------------')
    # Encabezado de la tabla con los nombres de los parques
    print(f"{'Medida':<20s} {'General Paz':<20s} {'Los Andes':<20s} {'Centenario':<20s}")
    print('----------------------------------------------------------------------------')
    print(f"{'Max':<20s} {max(lista_gral_paz):<20.2f} {max(lista_andes):<20.2f} {max(lista_centenario):<20.2f}")
    # Calculo el promedio de altura dividiendo la suma de todas las alturas por la cantidad de arboles
    print('----------------------------------------------------------------------------')
    print(f"{'Avg':<20s} {sum(lista_gral_paz)/len(lista_gral_paz):<20.2f} {sum(lista_andes)/len(lista_andes):<20.2f} {sum(lista_centenario)/len(lista_centenario):<20.2f}")
    print('----------------------------------------------------------------------------')

ESPECIE = 'Jacarandá'
imprimir_tabla_alturas(ESPECIE)

# Ejercicio 3.22

def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinaciones.append(int(arbol['inclinacio']))
    return inclinaciones

# Ejercicio 3.23

def especimen_mas_inclinado(lista_arboles):
    especies_en_lista = dict.fromkeys(especies(lista_arboles))
    for especie in especies_en_lista.keys():
        especies_en_lista[especie] = max(obtener_inclinaciones(lista_arboles, especie))
    ejemplar_mas_inclinado = max(especies_en_lista, key = especies_en_lista.get)
    return (ejemplar_mas_inclinado, especies_en_lista[ejemplar_mas_inclinado])

mas_inclinado_gral_paz = especimen_mas_inclinado(LISTA_ARBOLES_GRAL_PAZ)
mas_inclinado_andes = especimen_mas_inclinado(LISTA_ARBOLES_ANDES)
mas_inclinado_centenario = especimen_mas_inclinado(LISTA_ARBOLES_CENTENARIO)

print()
print(f'Especimen mas inclinado en General Paz: {mas_inclinado_gral_paz[0]} : {mas_inclinado_gral_paz[1]} grados')
print(f'Especimen mas inclinado en Los Andes: {mas_inclinado_andes[0]} : {mas_inclinado_andes[1]} grados')
print(f'Especimen mas inclinado en Centenario: {mas_inclinado_centenario[0]} : {mas_inclinado_centenario[1]} grados')

# Ejercicio 3.24

def especie_promedio_mas_inclinada(lista_arboles):
    especies_en_lista = dict.fromkeys(especies(lista_arboles))
    for especie in especies_en_lista.keys(): 
        inclinaciones = obtener_inclinaciones(lista_arboles, especie)
        especies_en_lista[especie] = sum(inclinaciones) / len(inclinaciones)
    especie_mas_inclinada = max(especies_en_lista, key = especies_en_lista.get)
    return (especie_mas_inclinada, especies_en_lista[especie_mas_inclinada])

especie_mas_inclinada_gral_paz = especie_promedio_mas_inclinada(LISTA_ARBOLES_GRAL_PAZ)
especie_mas_inclinada_andes = especie_promedio_mas_inclinada(LISTA_ARBOLES_ANDES)
especie_mas_inclinada_centenario = especie_promedio_mas_inclinada(LISTA_ARBOLES_CENTENARIO)

print()
print(f'Especie promedio mas inclinada en General Paz: {especie_mas_inclinada_gral_paz[0]} : {especie_mas_inclinada_gral_paz[1]} grados')
print(f'Especie promedio mas inclinada en Los Andes: {especie_mas_inclinada_andes[0]} : {especie_mas_inclinada_andes[1]} grados')
print(f'Especie promedio mas inclinada en Centenario: {especie_mas_inclinada_centenario[0]} : {especie_mas_inclinada_centenario[1]} grados')

# Imprime el ejemplar mas alto y el mas inclinado, con sus respectivas especies y coordenadas
with open(BASE_DE_DATOS, 'rt', encoding = 'utf-8') as f:
    rows = csv.reader(f)
    headers = next(rows)
    ejemplar_mas_inclinado_ciudad = ejemplar_mas_alto_ciudad = dict(zip(headers, next(rows))) 
    for row in rows:
        arbol = dict(zip(headers, row))
        if float(arbol['inclinacio']) > float(ejemplar_mas_inclinado_ciudad['inclinacio']):
            ejemplar_mas_inclinado_ciudad = arbol
        if int(arbol['altura_tot']) > int(ejemplar_mas_alto_ciudad['altura_tot']):
            ejemplar_mas_alto_ciudad = arbol
    print() 
    print(f"Ejemplar mas inclinado en toda la ciudad: {ejemplar_mas_inclinado_ciudad['nombre_com']} : {ejemplar_mas_inclinado_ciudad['inclinacio']} grados")
    print(f"Latitud: {ejemplar_mas_inclinado_ciudad['lat']}, Longitud: {ejemplar_mas_inclinado_ciudad['long']}")
    print()   
    print(f"Ejemplar mas alto en toda la ciudad: {ejemplar_mas_alto_ciudad['nombre_com']} : {ejemplar_mas_alto_ciudad['altura_tot']} metros")
    print(f"Latitud: {ejemplar_mas_alto_ciudad['lat']}, Longitud: {ejemplar_mas_alto_ciudad['long']}")