# ejercicio 12.10

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris

iris_dataset = load_iris()

# creamos un dataframe de los datos de flores
# etiquetamos las columnas usando las cadenas de iris_dataset.feature_names
iris_dataframe = pd.DataFrame(iris_dataset['data'],
                              columns=iris_dataset.feature_names)

iris_dataframe['target'] = iris_dataset['target']

# y hacemos una matriz de gráficos de dispersión, asignando colores según la especie
sns.pairplot(iris_dataframe, hue='target', diag_kind="hist")

plt.show()
