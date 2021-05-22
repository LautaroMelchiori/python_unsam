# vigilante.py
import os
import time

def vigilar(filename):
    f = open(filename)
    f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF

    while True:
        line = f.readline() # lee la ultima linea

        if line == '': # si la ultima linea no cambio
            time.sleep(0.5)   # Esperar un rato y
            continue          # vuelve al comienzo del while

        # si la ultima linea cambio (es decir que se agrego una nueva linea)
        # la entregamos
        yield line

if __name__ == '__main__':
    import informe

    camion = informe.leer_camion ('../Data/camion.csv')

    for line in vigilar('../Data/mercadolog.csv'):  
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])

        if nombre in camion:    
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')