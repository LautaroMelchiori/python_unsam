#lote.py

class Lote():
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    
    def __repr__(self) -> str:
        return f"Lote('{self.nombre}', {self.cajones}, {self.precio})"

    def costo(self):
        """
        Retorna el costo del lote (cajones * precio)
        """
        return self.cajones * self.precio

    def vender(self, n):
        """
        Reduce la cantidad de cajones en n
        """
        self.cajones -= n