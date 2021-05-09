import datetime

def dias_habiles(inicio, fin, feriados):
    """
    Calcula la cantidad de dias habiles entre dos fechas (inicio y fin)
    Feriados debe ser una lista de fechas de los dias feriados entre inicio y fin
    Todas las fechas deben ser inputeadas como texto y con formato dd/mm/yyyy

    Devuelve una lista con las fechas de dias habiles en el periodo [inicio: fin]
    """
    FORMATO = "%d/%m/%Y"

    # abreviamos las funciones strptime() y strftime()
    # de la clase datetime, del modulo datetime
    pasar_a_datetime = lambda x: datetime.datetime.strptime(x, FORMATO)
    pasar_a_str = lambda x: datetime.datetime.strftime(x, FORMATO)

    fecha_actual = pasar_a_datetime(inicio)
    fecha_final = pasar_a_datetime(fin)
    dias_habiles = []

    # pasamos los feriados a objetos datetime
    fechas_feriados = [pasar_a_datetime(feriado) for feriado in feriados]

    while fecha_actual != fecha_final:
        if fecha_actual.weekday() < 5 and fecha_actual not in feriados:
            dias_habiles.append(pasar_a_str(fecha_actual))
        
        # pasamos al siguiente dia
        fecha_actual = fecha_actual + datetime.timedelta(days = 1)

    if fecha_final.weekday() < 5 and fecha_final not in feriados:
            dias_habiles.append(pasar_a_str(fecha_final))

    return dias_habiles