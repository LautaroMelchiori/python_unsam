import datetime

def calcular_vida(b_day):
    """
    Recibe una fecha de nacimiento en formato 'dd/mm/AAAA'
    y devuelve la cantidad de segundos desde las 00:00hs de esa fecha
    """
    fecha = datetime.datetime.strptime(b_day, '%d/%m/%Y')
    hoy = datetime.datetime.now()
    segundos_transcurridos = fecha - hoy

    return abs(segundos_transcurridos.total_seconds())