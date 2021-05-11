import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns

dir_parques = os.path.join('..', 'data', 'arbolado-en-espacios-verdes.csv')
dir_veredas = os.path.join('..', 'data', 'arbolado-publico-lineal-2017-2018.csv')

df_parques = pd.read_csv(dir_parques)
df_veredas = pd.read_csv(dir_veredas)

# para seleccionar las columnas de diametro y altura
# usaremos el nombre que llevan estas en cada dataset
cols_sel_parques = ['diametro', 'altura_tot']
cols_sel_veredas = ['diametro_altura_pecho', 'altura_arbol']

df_tipas_parques = df_parques.loc[df_parques['nombre_cie'] == 'Tipuana Tipu', cols_sel_parques].copy()
df_tipas_veredas = df_veredas.loc[df_veredas['nombre_cientifico'] == 'Tipuana tipu', cols_sel_veredas].copy()

# unificamos nombres entre dataframes
df_tipas_veredas.rename(columns = {
    cols_sel_veredas[0] : cols_sel_parques[0],
    cols_sel_veredas[1] : cols_sel_parques[1]
    }, inplace = True)

# agregamos columna de ambiente para diferenciar
df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas['ambiente'] = 'vereda'

# juntamos dataframes en uno solo para graficar
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

# graficamos
df_tipas.boxplot('diametro',by = 'ambiente')
df_tipas.boxplot('altura_tot',by = 'ambiente')


# Modularizamos la comparacion entre ejemplares de una especie
def comparar(cienti_parques, cienti_veredas):
    """
    Compara el diametro y la altura de los ejemplares de una especie
    plantados en parques y en veredas

    cienti_parques debe ser el nombre cientifico con que se identifica
    a la especie en el dataset de parques (comuna 'nombre_cie')

    cienti_veredas debe ser el nombre cientifico con que se identifica
    a la especie en el dataset de veredas (columna 'nombre_cientifico')

    Genera 2 boxplots, uno comparando diametro y otro altura
    """

    df_especie_parques = df_parques.loc[df_parques['nombre_cie'] == cienti_parques, cols_sel_parques].copy()

    df_especie_veredas = df_veredas.loc[df_veredas['nombre_cientifico'] == cienti_veredas, cols_sel_veredas].copy()

    # unificamos nombres entre dataframes
    df_especie_veredas.rename(columns = {
        cols_sel_veredas[0] : cols_sel_parques[0],
        cols_sel_veredas[1] : cols_sel_parques[1]
        }, inplace = True)

    df_especie_parques['ambiente'] = 'parque'
    df_especie_veredas['ambiente'] = 'vereda'

    df_especie = pd.concat([df_especie_veredas, df_especie_parques])

    df_especie.boxplot('diametro',by = 'ambiente')
    df_especie.boxplot('altura_tot',by = 'ambiente')

plt.show()