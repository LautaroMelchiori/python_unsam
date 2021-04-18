cadena = 'Geringoso'
cadena_transformada = ''

for letra in cadena:
    cadena_transformada += letra
    if letra in 'aeiou':
        cadena_transformada += 'p' + letra

print(cadena_transformada)
        