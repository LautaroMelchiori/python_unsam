# sec_binarias.py

# Implementacion propia de incrementar
# Complejidad lineal --> O(n)
def incrementar(s):
    """
    Recibe una secuencia binaria y devuelve la siguiente
    """
    siguiente = s.copy()
    for i in range(len(s) - 1, -1, -1):
        if s[i] == 0:
            siguiente[i] = 1
            return siguiente
        else:
             siguiente[i] = 0
    return siguiente

# Devuelve todas las secuencias binarias de longitud n posibles (seran 2^n)
# Complejidad exponencial --> O(2^n)
# Funcion exponencial
def listar_secuencias(n):
    """
    Devuelve una lista de todas las secuencias binarias de longitud n posibles
    """
    secuencias = [[0] * n]
    sec_actual = secuencias[0]
    # La cantidad de secuencias binarias de longitud n es igual a 2^n, y restamos 1 ya que la primera fue introducida manualmente
    for _ in range(2 ** n - 1):
        sec_incrementada = incrementar(sec_actual)
        sec_actual = sec_incrementada
        secuencias.append(sec_incrementada)
    return secuencias