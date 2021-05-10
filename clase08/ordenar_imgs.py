import datetime
import os
import sys

def procesar_nombre(nombre):
    """
    Recibe el nombre de un archivo y devuelve la fecha que contiene
    y el nombre procesado (sin el guion bajo ni la fecha)

    El nombre del archivo debe contener en sus ultimos 8 caracteres la fecha
    en formato AAAAMMDD

    Se devuelve una tupla con la fecha y el nombre
    La fecha es devuelta como un objeto de la clase datetime, del modulo datetime
    El nombre se devuelve como una string
    """
    # sabiendo que la fecha esta en los ultimos 8 caracteres
    # antes de la extension de archivo y en formato AAAAMMDD, la extraemos
    fecha = datetime.datetime.strptime(nombre[-12:-4], '%Y%m%d')

    # sacamos los ultimos 13 caracteres (1 guion, 8 de fecha y 4 de ext. de archivo)
    # y volvemos a poner la extension de archivo
    nombre_procesado = nombre[:-13] + '.png'

    return fecha, nombre_procesado


def procesar_img(archivo, path, destino):
    """
    Recibe el nombre de un archivo y su path y lo procesa
    Procesar es:
    - leer la fecha codificada en su nombre
    - usar esa fecha para setear la ultima modificacion
    - cambia el nombre del archivo eliminando la fecha
    - mueve el archivo al directorio destino
    """
    fecha, nombre_procesado = procesar_nombre(archivo)

    # modificamos la fecha de acceso y modificacion
    ts_fecha = fecha.timestamp()
    os.utime(path, (ts_fecha, ts_fecha))

    # cambiamos el nombre de archivo y lo movemos al destino
    os.rename(path, os.path.join(destino, nombre_procesado))

        

def main(original, destino):
    # Creamos el directorio destino si no existe
    if not os.path.isdir(destino):
        os.mkdir(destino)

    # recorremos todo el directorio original y sus subdirectorios
    # extrayendo imagenes y procesandolas
    for root, dirs, files in os.walk(original):
        for f in files:
            if f[-4:] == '.png':
                path = os.path.join(root, f)
                procesar_img(f, path, destino)
    
    # recorremos nuevamente el directorio original y sus subdirectorios,
    # esta vez de abajo para arriba, eliminando los directorios vacios
    for root, dirs, files in os.walk(original, topdown = False):
        for d in dirs:
            path = os.path.join(root, d)
            if not os.listdir(path):
                os.rmdir(path)


if __name__ == '__main__':
    import sys
    # el primer parametro sera el directorio a procesar y el segundo el destino
    main(sys.argv[1], sys.argv[2])