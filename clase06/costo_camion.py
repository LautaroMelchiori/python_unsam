# costo_camion.py
import informe_funciones

# Ejercicio 6.12
def costo_camion(archivo_camion):
    camion = informe_funciones.leer_camion(archivo_camion)
    total = 0
    for lote in camion:
        total += lote['cajones'] * lote['precio']
    print(f'Costo total {total}')