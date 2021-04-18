# espacio inicial
print("    ", end='')

# imprimir los numeros del 0 al 9, dedicandole 3 espacios a cada numero
print(*(f"{n:3}" for n in range(10)))

# linea divisora
print(f'-------------------------------------------')

# imprimir las filas del 0 al 9
for fila in range(10):
    # poner el numero de la fila y espaciar
    print(f"{fila}:  ", end='')
    # completar con la tabla de cada numero multiplicando el numero actual por la columna
    print(*(f"{fila*columna:3}" for columna in range(10)))