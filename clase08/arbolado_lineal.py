import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']

direc = os.path.join('..', 'data', 'arbolado-publico-lineal-2017-2018.csv')

df_lineal = pd.read_csv(direc, usecols = cols_sel)

especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']

df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]

df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')
df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')

sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')

plt.show()