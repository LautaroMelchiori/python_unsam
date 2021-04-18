def costo_camion(archivo):
    with open(archivo, 'rt') as f:
        headers = next(f)
        total = 0
        for line in f:
            current_line = line.split(',')
            total += float(current_line[1]) * float(current_line[2])
    return total

costo = costo_camion('../Data/camion.csv')
print(f'Costo total {costo}')