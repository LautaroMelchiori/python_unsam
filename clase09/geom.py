class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    # Used with `repr()`
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'

    def __add__(self, b):
      return Punto(self.x + b.x, self.y + b.y)

def calcular_esquinas(esq1, esq2):
    """
    Recibe dos esquinas opuestas de un cuadrilatero
    Calcula las 4 esquinas del cuadrilatero y las devuelve
    """
    return Punto(esq1.x, esq2.y), Punto(esq2.x, esq1.y), Punto(esq1.x, esq1.y), Punto(esq2.x, esq2.y)

def identificar_esquinas(corners):
    """
    Recibe los cuatro vertices de un cuadrilatero
    Devuelve el vertice superior izq., superior der.,
    inferior izq., inferior der., en ese orden
    """
    xs = [corner.x for corner in corners]
    ys = [corner.y for corner in corners]
    max_x = max(xs)
    max_y = max(ys)
    min_x = min(xs)
    min_y = min(ys)

    # identificamos esquinas
    for corner in corners:
        if corner.x == max_x and corner.y == min_y:
            br = corner
        elif corner.x == min_x and corner.y == min_y:
            bl = corner
        elif corner.x == max_x and corner.y == max_y:
            tr = corner
        elif corner.x == min_x and corner.y == max_y:
            tl = corner

    return tl, tr, bl, br

class Rectangulo():
    def __init__(self, corner1, corner2):
        self.tl, self.tr, self.bl, self.br = identificar_esquinas(calcular_esquinas(corner1, corner2))

    def __repr__(self):
        return f'{self.tl}{self.tr}{self.bl}{self.br}'

    def __str__(self):
        laterales = ['|' + ' ' * (self.base() - 2) + '|' for _ in range(self.altura())]
        laterales = '\n'.join(laterales)

        return f"{'-' * self.base()}\n{laterales}\n{'-' * self.base()}"

    def base(self):
        return abs(self.br.x - self.bl.x)

    def altura(self):
        return abs(self.tl.y - self.bl.y)

    def area(self):
        return self.base() * self.altura()

    def desplazar(self, desplazamiento):
        self.tl += desplazamiento
        self.tr += desplazamiento
        self.bl += desplazamiento
        self.br += desplazamiento

    def rotar(self):
        """
        Rota el rectangulo 90 grados para la derecha, 
        sobre la esquina inferior derecha del mismo
        """
        base = self.base()
        altura = self.altura()

        # Rotamos la esquina superior izquierda
        self.tl.y += base - altura
        self.tl.x += base + altura

        # Teniendo la esquina inferior derecha (que no cambia)
        # Y la superior izquierda ya modificada, volvemos a construir
        # el rectangulo llamando al constructor dandole dos esquinas opuestas
        self.__init__(self.tl, self.br)