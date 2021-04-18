def invertir_lista(lista):
    lista_invertida = []
    for elemento in lista:
        # Agregamos cada nuevo elemento al principio de la lista
        lista_invertida.insert(0, elemento)
    
    return lista_invertida

# input: invertir_lista([1, 2, 3, 4, 5])
# output: [5, 4, 3, 2, 1]

# input: invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])
# output: ['San Miguel', 'San Fernando', 'Santiago', 'Rosario', 'Bogotá']