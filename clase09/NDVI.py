import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.colors

# Ejercicio 9.15
def crear_img_png(carpeta, nombre_banda, nombre = False):
    """
    Recibe una carpeta y un numero de banda
    Muestra una imagen de dicha banda y la guarda en un png

    banda: nombre de archivo .npy conteniendo una matriz
           de los valores de la banda
           
    Se puede especificar el nombre del archivo png,
    si no se hace, el nombre default sera el de la banda
    """
    banda = np.load(os.path.join(carpeta, nombre_banda))
    q = 1
    vmin = np.percentile(banda.flatten(), q)
    vmax = np.percentile(banda.flatten(), 100 - q)

    plt.figure()
    im = plt.imshow(banda, vmin = vmin, vmax = vmax)
    plt.colorbar(im)

    if not nombre:
        nombre = nombre_banda
    
    plt.savefig(f'{nombre[:-4]}_IMG.png')
    #plt.show()

# crear_img_png('../../clip', 'LC08_L1TP_225084_20180213_20180222_01_T1_sr_band1_clip.npy')

# Ejercicio 9.16
def crear_hist_png(carpeta, nombre_banda, bins, nombre = False):
    """
    Recibe una carpeta y un numero de banda
    Muestra un histograma de los valores de 
    dicha banda y la guarda en un png

    banda: nombre de archivo .npy conteniendo una matriz
           de los valores de la banda

    Se puede especificar el nombre del archivo png,
    si no se hace, el nombre default sera el de la banda
    """
    banda = np.load(os.path.join(carpeta, nombre_banda))
    plt.figure()
    plt.hist(banda.flatten(), bins = bins)

    if not nombre:
        nombre = nombre_banda
    
    plt.savefig(f'{nombre[:-4]}_BIN.png')
    #plt.show()

# crear_hist_png('../../clip', 'LC08_L1TP_225084_20180213_20180222_01_T1_sr_band1_clip.npy', 100)

# Ejercicio 9.17
def crear_imgs_hist_bandas():
    for i in range(1,8):
        crear_img_png('../../clip', f'LC08_L1TP_225084_20180213_20180222_01_T1_sr_band{i}_clip.npy')
        crear_hist_png('../../clip', f'LC08_L1TP_225084_20180213_20180222_01_T1_sr_band{i}_clip.npy', 100)

# Elegi la banda 5 para el experimento, 
# y setie el umbral en 1 tras ver el histograma
banda = np.load(os.path.join('..', '..', 'clip', 'LC08_L1TP_225084_20180213_20180222_01_T1_sr_band5_clip.npy'))
umbral = 1

# los elementos que esten por encima del umbral seran 1
# los que no, seran 0
banda_bin = banda >= umbral

# ploteamos la banda normal y la binaria para ver bien la diferencia
figure = plt.figure()

plot_normal = plt.subplot(2,1,1)
plot_normal.title.set_text('Banda Normal')
plt.imshow(banda)

plot_bin = plt.subplot(2,1,2)
plot_bin.title.set_text('Banda Binaria')
plt.imshow(banda_bin)

# añadimos padding para ver mejor los ploteos
figure.tight_layout(pad=3.0)

plt.show()

# tras graficar vemos que un tipo de pixel
# correspondia a la superficie terrestre
# y el otro tipo de pixel correspondia a las areas con agua

# Ejercicio 9.18

# banda de rojo
bR = np.load(os.path.join('..', '..', 'clip', 'LC08_L1TP_225084_20180213_20180222_01_T1_sr_band5_clip.npy'))

# banda de infrarojo cercano
bNIR = np.load(os.path.join('..', '..', 'clip', 'LC08_L1TP_225084_20180213_20180222_01_T1_sr_band4_clip.npy'))

# calculamos NDVI y truncamos posibles problemas
ndvi = (bR - bNIR) / (bR + bNIR)
ndvi[ndvi > 1] = 1
ndvi[ndvi < -1] = -1

# usando el valor de ndvi asignamos un numero de categoria a cada pixel
# luego usaremos estas categorias para diferenciar entre zonas segun su nivel de vegetacion
clases_ndvi = np.ndarray(ndvi.shape)

# areas no vegetadas
clases_ndvi[ndvi <= 0] = 0

# areas desnudas
mask = np.logical_and(ndvi > 0, ndvi <= 0.1)
clases_ndvi[mask] = 1

# areas con vegetacion baja
mask = np.logical_and(ndvi > 0.1, ndvi <= 0.25)
clases_ndvi[mask] = 2

# areas con vegetacion moderada
mask = np.logical_and(ndvi > 0.25, ndvi <= 0.4)
clases_ndvi[mask] = 3

# areas con vegetacion densa
clases_ndvi[ndvi > 0.4] = 4

q = 1    
vmin = np.percentile(clases_ndvi.flatten(), q)
vmax = np.percentile(clases_ndvi.flatten(), 100 - q)
color_map = matplotlib.colors.ListedColormap(['black', 'y', 'yellowgreen', 'g', 'darkgreen'])
plt.imshow(clases_ndvi, cmap = color_map, vmin = vmin, vmax = vmax)

plt.show()