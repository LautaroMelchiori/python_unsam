def buscar_precio(fruta):
    fruta_figura = False
    with open('../Data/precios.csv', 'rt') as f:
        for linea in f:
            info_fruta_actual = linea.split(',')
            if info_fruta_actual[0] == fruta:
                print(f'El precio de un cajón de {fruta} es: {info_fruta_actual[1]}')
                fruta_figura = True
                break
    
    if not fruta_figura:
        print(f'{fruta} no figura en el listado de precios.')