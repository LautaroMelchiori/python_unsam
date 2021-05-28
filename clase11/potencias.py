# ej 11.4

def es_potencia(n, b, acumulado = 1):
    """
    Recibe 2 enteros, n y b, 
    Devuelve True si n es potencia de b
    False de lo contrario
    """

    if acumulado == n:
        return True
    elif abs(acumulado) > abs(n):
        return False
    
    return es_potencia(n, b, acumulado * b)