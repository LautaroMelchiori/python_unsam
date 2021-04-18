#solucion_de_errores.py
# Ejercicios de errores en el codigo

#%%
# Ejercicio 3.1. Funcion tiene_a()
# Comentario: El error era de tipo semantico y estaba ubicado en la linea 7
# Ese 'else' hace que a la primera letra que se checkea y no es una 'a' se retorne False, saliendo de la funcion y no permitiendo que se termine de checkear el resto de la palabra
# Lo corregi quitando ese else de adentro del loop y solamente retornando False despues del while, una vez que ya se checkearon todas las letras a ver si alguna era una 'a'
# A continuacion va el codigo de la funcion corregido:

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
# Ejercicio 3.2 Funcion tiene_a()
# Comentario: El erorr aca era de tipo sintactico, y esta ubicado en la linea 8
# Lo que sucede es que en vez de retornarse False (valor booleano) se retorna 'Falso', que no es nada
# Lo corregi escribiendo bien la palabra False
# A continuacion va el codigo de la funcion corregido:

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%
# Ejercicio 3.3 Funcion tiene_uno()
# Comentario: Los errores aca son de tipo, y estan ubicados en las lineas 2 y 6
# El codigo en estas dos lineas asume que el parametro ingresado a la funcion es un objeto iterable, como una string, de lo contrario alzaran un TypeError
# Lo corregi transformado el parametro en una string, asi nos aseguramos que trabajamos con una y no tendremos problemas cuando se ingrese un numero a la funcion
# A continuacion va el codigo corregido:

def tiene_uno(parametro):
    expresion = str(parametro)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

#%%
# Ejercicio 3.4 Funcion suma(a, b)
# Comentario: El error aca se da por un tema de scope de variables
# Lo que pasa es que la funcion hace la suma y la guarda en una varible local c, cuyo valor solo es accesible desde dentro de la funcion
# Para que un valor generado dentro de una funcion pueda ser usado fuera de ella, la funcion debe retornarlo con un return
# Asi que modifique el codigo de la funcion para que en lugar de almacenar el resultado de la suma en una variable local, lo retorne
# A continuacion va el codigo corregido:

def suma(a,b):
    return a + b
a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
# Ejercicio 3.5
# Comentario: El error aca se da porque el codigo modifica una y otra vez el mismo objeto, pisando lo que habia antes, en lugar de crear uno nuevo para cada fila
# Lo que sucede es que se crea el objeto "registro" una vez en el codigo, y cada iteracion del loop modifica el objeto ya existente y agrega una referencia a este a la lista
# Lo que hice para corregir el codigo fue crear un nuevo diccionario en cada iteracion del loop y agregarlo a la lista de registros, asi quedando todos diccionarios diferentes, uno para cada fruta y su informacion
# A continuacion va el codigo corregido:

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)