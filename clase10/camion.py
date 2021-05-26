# camion.py

class Camion:

    def __init__(self, lotes):
        """
        Asumimos que el camion sera inicializado con una lista de Lotes
        """
        self.lotes = lotes

    def __len__(self):
        return len(self.lotes)

    def __iter__(self):
        return self.lotes.__iter__()

    def __add__(self, lote):
        # aca se presupone que el camion ya tiene lotes en el cargamento
        # entonces se chequea que el elemento que estamos queriendos sumar
        # sea del tipo Lote
        if isinstance(lote, type(self.lotes[0])):
            return self.lotes + [lote]
    
    def __contains__(self, key):
        return key in (lote.nombre for lote in self.lotes)
    
    def __getitem__(self, index):
        return self.lotes[index]

    def __repr__(self):
        return f'{self.lotes}'
    
    def agregar(self, lote):
        """
        Recibe un lote (objeto de la clase Lote) y lo agrega al camion
        """
        self.lotes.append(lote)
        
    def precio_total(self):
        return sum(l.costo() for l in self.lotes)

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total