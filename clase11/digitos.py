# ej 11.3

def dig(n):
    """
    Recibe un numero n (int or float)
    Devuelve la cantidad de digitos del mismo
    """

    def dig_aux(n):
        if n < 10:
            return 1

        return 1 + dig_aux(n /10)

    return dig_aux(abs(n))