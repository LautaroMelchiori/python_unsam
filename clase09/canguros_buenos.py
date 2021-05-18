# Ejercicio 9.11

class Canguro():
    def __init__(self):
        self.contenido_marsupio = []

    def meter_en_marsupio(self, obj):
        """
        Agrega el objeto 'obj' al marsupio
        """
        self.contenido_marsupio.append(obj)
    
    def __str__(self):
        return f'Canguro. Contenido del marsupio: {self.contenido_marsupio}'

    def __repr__(self):
        return f'Canguro()'

'''
# canguro_malo.py
Este código continene un 
bug importante y dificil de ver


# El problema se hallaba en el constructor, 
# el cual si no recibia un parametro
# 'contenido', lo asociaba a una lista vacia

# El problema es que ese objeto de lista vacia 
# era el mismo para todos los objetos
# que se inicializaban sin contenido

# Entonces el atributo contenido_marsupio 
# de todos los objetos inicializados sin contenido
# Apuntaba al mismo objeto => al cambiar este objeto 
# modificando el atributo en un objeto lo cambiabamos en todos

# Lo solucionamos facilmente creando un nuevo objeto de lista vacia
# para cada objeto que se inicialice sin contenido inicial


class Canguro:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre, contenido=[]):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        if not contenido:
            self.contenido_marsupio = []
        else:
            self.contenido_marsupio = contenido

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)


madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)

# Al ejecutar este código todo parece funcionar correctamente.
# Para ver el problema, imprimí el contenido de cangurito.

'''