def costo_camion(archivo):
    with open(archivo, 'rt') as f:
        headers = next(f)
        total = 0
        current_line = 0
        for line in f:
            current_line += 1
            fields = line.split(',')
            try:
                total += float(fields[1]) * float(fields[2])
            except ValueError:
                print(f'Advertencia: Hay datos faltantes en la linea {current_line}')
    return total

costo = costo_camion('../Data/camion.csv')
print(f'Costo total {costo}')