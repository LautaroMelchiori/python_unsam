import datetime

def reincorporacion(dias = 200, fecha = '26/09/2020'):
    """
    Calcula que dia te reincorporarias a tu trabajo
    si te tomas una licencia de "dias" dias el dia "fecha"
    Los dias deben ser un numero entero, y la fecha debe estar en formato "dd/mm/yyyy"

    Si no se especifican los dias, seran 200
    Si no se especifica la fecha, sera el 26/09/2020
    """

    date = datetime.datetime.strptime(fecha, "%d/%m/%Y")
    days = datetime.timedelta(days = dias)

    return datetime.datetime.strftime(date + days, '%d/%m/%Y')