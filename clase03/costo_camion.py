import csv

CAMION = '../Data/fecha_camion.csv'

def costo_camion(nombre_archivo):
    costo = 0.0
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        encabezados = next(rows)
        for row_number, row in enumerate(rows, start = 1):
            record = dict(zip(encabezados, row))
            try:
                cajones = int(record['cajones'])
                precio = float(record['precio'])
                costo += cajones * precio
            # Manejamos el error que puede surgir en caso de faltar informacion en el archivo
            except ValueError:
                print(f'Fila {row_number}: No pude interpretar {row}')
                continue
    return costo

print(f'Costo total: {costo_camion(CAMION)}')