import math

# Pedimos el radio y nos aseguramos de que sea un numero
while True:
    radio = input('Ingrese el radio de la esfera de la cual queramos saber el volumen: ')
    if radio.isnumeric():
        break

# Calculamos el volumen de la esfera con la formula 4/3 * pi * radio^3
print('El volumen de la esfera es:', (4/3) * math.pi * (float(radio) ** 3))