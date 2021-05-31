# ejercicio 11.13

def hojas(n):
    """
    Devuelve las medidas de una hoja A(n) segun la norma ISO 216
    """
    def hojas_aux(n):
        if n == 0:
            return 841, 1189
        
        medidas_anterior = hojas_aux(n - 1)

        return (medidas_anterior[1] // 2, medidas_anterior[0])

    medidas = hojas_aux(n)
    print(f"{medidas[0]} x {medidas[1]} mm")