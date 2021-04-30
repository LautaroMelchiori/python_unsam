# sumas.py

# Ejercicio 7.6

# Definicion con ciclo

def sumar_enteros(desde, hasta):
    '''
    Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''

    if hasta < desde:
        return 0

    suma_total = 0
    for i in range(desde, hasta + 1):
        suma_total += i
    
    return suma_total

# Definicion en tiempo constante

def triangular(n):
    """
    Calcula la cantidad de objetos dispuestos en un triangulo equilatero cuyo lado tiene n-objetos
    
    Pre: n debe ser un numero entero y positivo
    Pos: Se devuelve el valor de sumar todos los números del intervalo [1, n]
    """

    return int((n * (n+1)) / 2)

def sumar_enteros_const(desde, hasta):
    '''
    Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''

    if hasta < desde:
        return 0

    return triangular(hasta) - triangular(desde - 1)