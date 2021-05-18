# Torre de control

class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0
    
class TorreDeControl():
    def __init__(self):
        self.aterrizajes = Cola()
        self.despegues = Cola()

    def nuevo_arribo(self, arribo):
        """
        Recibe un arribo en forma de String
        y lo añade a la lista de aviones por aterrizar
        """
        self.aterrizajes.encolar(arribo)

    def nueva_partida(self, partida):
        """
        Recibe una nueva partida en forma de String
        y lo añade a la lista de aviones por despegar
        """
        self.despegues.encolar(partida)
    
    def ver_estado(self):
        """
        Imprime el estado actual de la torre,
        con los aviones en espera para aterrizas y despegar
        """
        at = 'Vuelos esperando para aterrizar: '
        des = 'Vuelos esperando para despegar: '

        at += ', '.join(self.aterrizajes.items)
        des += ', '.join(self.despegues.items)
        print(at)
        print(des)
    
    def asignar_pista(self):
        if self.aterrizajes.esta_vacia():
            if self.despegues.esta_vacia():
                print('No hay vuelos en espera.')
                return
            vuelo = self.despegues.desencolar()
            print(f'El vuelo {vuelo} despegó con exito.')
        else:
            vuelo = self.aterrizajes.desencolar()
            print(f'El vuelo {vuelo} aterrizó con exito.')

        