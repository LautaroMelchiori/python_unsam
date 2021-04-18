# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:22:56 2021

@author: lavir
"""

# fun_zip.py 3.9
#%% Primer prueba
"""
from pprint import pprint
import csv
f = open('../Data/camion.csv')
filas = csv.reader(f)
g=[]
encabezado = next(filas)
for fila in filas:
    d=dict(zip(encabezado,fila))
    g.append(d)
pprint(g)

#%% Segunda prueba

def costo_camion(nombre_archivo):
    import csv
    total = 0
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for n,fila in enumerate(filas,start=1):
            record = dict(zip(encabezado,fila))
            try:
                precio = float(record['precio']) * int(record['cajones'])
                total += precio
            except ValueError:
                print(f'Fila {n}: No pude interpretar: {fila}')
    return total
dou = costo_camion('../Data/fecha_camion.csv')
print(dou)
"""
#%% Tercer prueba

import csv
def leer_precios():
    with open("../Data/precios.csv") as file:
        rows = csv.reader(file)
        frutas=[]
        precios = []
        '''
        Esta es la parte que genera un error,
        intentas desempacar fruta y precio de la variable 'rows' la cual es un objeto reader

        for fruta, precio in rows:
            frutas.append(fruta)
            precios.append(precio)
        '''
        
        # Lo que hay que hacer es ITERAR sobre el objeto reader, accediendo a cada fila del archivo
        for row in rows:
            try:
                frutas.append(row[0])
                precios.append(row[1])
            # manejamos el error que puede surgir si aparece una linea vacia
            except IndexError:
                continue

    precios = dict(zip(frutas,precios))
    return precios
    
def leer_camion():
    camion = []
    with open('../Data/camion.csv') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            lote = dict(zip(headers,row))
            camion.append(lote)
    return camion

precios = leer_precios()
costo_camion = 0
recaudacion = 0
camion_leido = leer_camion()
for a in camion_leido: #Costo camion
    costo_camion += int(a['cajones']) * float(a['precio'])
for b in camion_leido: #Dinero recaudado
    recaudacion += float(precios[b['nombre']]) * int(b['cajones'])
resultado = float(round(recaudacion - costo_camion,2))
if resultado <0:           #Me dice si hubo ganancias o perdidas
    estado = "Perdidas"
else:
    estado = 'Ganancias'
print(f'Costo de camión: {costo_camion} | Recaudación: {recaudacion} | {estado}: {resultado}')