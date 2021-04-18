def propagar(lista):
    # Vamos tomando en cuenta el estado actual del fuego
    # Arranca apagado, se prende al llegar a un fosforo prendido, y se apaga al llegar a un fosforo carbonizado
    hay_fuego = False
    # Llevamos una lista con los indices de todos los fosforos que pueden llegar a ser encendidos
    fosforos_nuevos = []
    # Creamos una copia de la lista introducida a la cual iremos modificando para simular la propagacion
    lista_propagada = list(lista)
    for indice, fosforo in enumerate(lista):
        # Si encontramos un fosforo prendido fuego, actualizamos la variable de hay_fuego
        if fosforo == 1:
            hay_fuego = True
            # Al haber encontrado fuego, todos los fosforos nuevos que venian detras del encendido deben ser prendidos
            for fosforo in fosforos_nuevos:
                lista_propagada[fosforo] = 1
        # Si encontramos un fosforo nuevo y hay fuego, lo prendemos
        elif fosforo == 0:
            if hay_fuego:
                lista_propagada[indice] = 1
            # Si no hay fuego, lo agregamos a la lista de fosforos nuevos que seran encendidos en caso de que aparezca fuego mas adelante
            else:
                fosforos_nuevos.append(indice)
        # Si encontramos un fosforo carbonizado, deja de haber fuego 
        # y dejamos de guardar los fosforos nuevos que habia hasta ese punto ya que no seran encendidos
        else:
            hay_fuego = False
            fosforos_nuevos = []

    return lista_propagada

# input: propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
# output: [0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]

# input: propagar([ 0, 0, 0, 1, 0, 0])
# output: [1, 1, 1, 1, 1, 1]