# ej 11.6

def par(n):
    """
    Recibe un numero natural
    
    Devuelve True si es par
    """
    
    if n == 1:
        return False
    
    return not par(n - 1)

def impar(n):
    """
    Recibe un numero natural

    Devuelve True si es impar
    """
    return not par(n)
