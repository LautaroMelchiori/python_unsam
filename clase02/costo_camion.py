with open('../Data/camion.csv', 'rt') as f:
    headers = next(f)
    total = 0
    for line in f:
        current_line = line.split(',')
        total += float(current_line[1]) * float(current_line[2])
    print(f'Costo total {total}')