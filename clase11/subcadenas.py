# ej 11.5

def posiciones_de(string, sub):
    """
    Recibe una cadena string y una subcadena sub

    Devuelve las posiciones de inicio de las apariciones
    de la subcadena en la cadena

    Ejemplo: posiciones_de('Un tete a tete con Tete', 'te') -> [3, 5, 10, 12, 21]
    """
    
    def posiciones_de_aux(string, sub, pos = [], idx = 0):
        if idx + 1 >= len(string):
            return pos

        if string[idx : idx + len(sub)] == sub:
            pos.append(idx)
            return posiciones_de_aux(string, sub, pos, idx + len(sub) - 1)
        else:
            return posiciones_de_aux(string, sub, pos, idx + 1)

    return posiciones_de_aux(string, sub)