class Pila():
    def __init__(self):
        self.items = []

    def apilar(self, obj) -> None:
        """
        Recibe un objeto y lo apila
        """
        self.items.append(obj)
    
    def desapilar(self) -> object:
        """
        Desapila y devuelve el ultimo elemento
        """
        return self.items.pop()

    def esta_vacia(self):
        """
        Devuelve True si la pila esta vacia,
        False si no
        """
        return len(self.items) == 0

def mostrar_x_del_estado(estado):
    print(f"Ejecutando {estado['función']}(), x vale {estado['variables']['x']}")