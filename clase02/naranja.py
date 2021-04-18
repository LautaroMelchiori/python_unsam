with open('../Data/precios.csv', 'rt') as f:
    for fruit in f:
        current_fruit = fruit.split(',')
        if current_fruit[0] == 'Naranja':
            print(f'El precio de la naranja es: {current_fruit[1]}')
            break
            