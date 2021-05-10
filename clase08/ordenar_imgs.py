import datetime
import os
import sys

# el primer parametro sera el directorio a procesar y el segundo el destino
original = sys.argv[1]
destino = sys.argv[2]

# Creamos el directorio destino si no existe
if not os.path.isdir(destino):
    os.mkdir(destino)

