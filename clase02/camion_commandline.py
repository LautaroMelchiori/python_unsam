import csv
import sys

def costo_camion(archivo):
    with open(archivo) as f:
        rows = csv.reader(f)
        headers = next(rows)
        total = 0
        current_row = 0
        for row in rows:
            current_row += 1
            try:
                total += float(row[1]) * float(row[2])
            except ValueError:
                print(f'Advertencia: Hay datos faltantes o incorrectos en la linea {current_row}')
    return total

archivo = sys.argv[1] if len(sys.argv) == 2 else '../Data/camion.csv'

costo = costo_camion(archivo)
print(f'Costo total {costo}')