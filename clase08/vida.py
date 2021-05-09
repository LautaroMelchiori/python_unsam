import datetime

# Ejercicio 8.1

def segundos_transcurridos(fecha):
    """
    Recibe una fecha en formato 'dd/mm/AAAA'
    y devuelve la cantidad de segundos desde las 00:00hs de esa fecha
    """
    date = datetime.datetime.strptime(fecha, '%d/%m/%Y')
    now = datetime.datetime.now()
    segundos_transcurridos = date - now

    return abs(segundos_transcurridos.total_seconds())