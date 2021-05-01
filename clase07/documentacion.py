# documentacion.py

# Ejercicio 7.8


def valor_absoluto(n):
    """
    Retorna el valor absoluto de un numero

    Pre: N debe ser un numero
    Pos: Se devolvera la distancia de ese numero al 0 en una recta numerica
    """
    if n >= 0:
        return n
    else:
        return -n


def suma_pares(l):
    """
    Retorna la suma de todos los numeros pares en 'l'
    Si 'l' esta vacia o no contiene numeros pares, retorna 0

    Pre: 'l' debe ser una lista compuesta unicamente por numeros
    Pos: Se devolvera la suma de todos los valores contenidos en 'l'
         que sean multiplos de 2

    Invariante de ciclo: 'res' es igual a la suma de todos los numeros pares
                         contenidos en la porcion ya recorrida de la lista
    """
    res = 0
    for e in l:
        if e % 2 == 0:
            res += e
        else:
            res += 0

    return res

def veces(a, b):
    """
    Retorna el resultado de sumar 'b' veces el valor de 'a'
    
    Pre: 'a' y 'b' deben ser numeros
    Pos: Se devolvera el producto de 'a' y 'b'

    Invariante de ciclo: 'res' es igual a el producto entre b - nb y a
    """
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res


def collatz(n):
    """
    Calcula la cantidad de sucesiones necesarias para llegar a 1
    partiendo de 'n' y aplicando la conjetura de collatz

    Pre: 'n' es un entero positivo
    Pos: devuelve la cantidad de pasos que tomó llegar a 1 
         aplicando la conjetura de collatz
    
    Invariante de ciclo: 'res' es la cantidad de pasos que dimos hasta ahora,
    y 'n' es el numero en el que nos encontramos actualmente
    """
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res