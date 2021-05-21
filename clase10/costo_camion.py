# costo_camion.py
import informe

# Ejercicio 6.12

def costo_camion(archivo_camion):
    camion = informe.leer_camion(archivo_camion)
    print(f'Costo total {camion.precio_total()}')

# Ejercicio 7.2 y 7.3

def main(parametros):
    costo_camion(parametros[1])

if __name__ == '__main__':
    import sys
    main(sys.argv)