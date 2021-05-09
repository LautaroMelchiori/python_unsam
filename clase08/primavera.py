import datetime

def cuanto_falta(fecha = False):
    """
    Calcula el tiempo faltante desde ahora hasta fecha
    Si no se introduce una fecha, devuelve cuanto falta 
    para la proxima primavera (del hemisferio sur)
    """
    ahora = datetime.datetime.now()
    if fecha == False:
        fecha = datetime.datetime.strptime(f'22/09/{ahora.year}', '%d/%m/%Y')
    tiempo_faltante = fecha - ahora
    
    # sumamos 1 para contar el dia que esta transcurriendo actualmente
    return tiempo_faltante.days + 1