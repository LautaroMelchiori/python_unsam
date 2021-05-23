import datetime
import os
import sys

path = sys.argv[1]

def generador(root, files):
    for f in files:
        if f[-4:] == '.png':
            viejos = f'{root}/{f}'

            nuevo_nombre = f[:-13] + '.png'
            nuevos = f'imgs_procesadas/{nuevo_nombre}'

            fecha = datetime.datetime.strptime(f[-12:-4], '%Y%m%d')

            yield (viejos, nuevos, fecha)

for root, dirs, files in os.walk(path):
    for f in generador(root, files):
        print(f)