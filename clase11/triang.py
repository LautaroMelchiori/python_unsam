# ej 11.2

def triang(n):
    """
    Calcula recursivamente el n-esimo numero triangular
    """
    if n == 1:
        return 1
    
    return n + triang(n - 1)