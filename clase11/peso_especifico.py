# ejercicio 11.15

import requests
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import io

enlace = 'https://raw.githubusercontent.com/python-unsam/Programacion_en_Python_UNSAM/master/Notas/11_Recursion/longitudes_y_pesos.csv'
r = requests.get(enlace).content
data_lyp = pd.read_csv(io.StringIO(r.decode('utf-8')))

ajus = linear_model.LinearRegression(fit_intercept = False) # llamo al modelo de regresión lineal
ajus.fit(data_lyp[['longitud']], data_lyp['peso']) # ajusto el modelo

grilla_x = np.linspace(start = 0, stop = 27, num = 25)
grilla_y = ajus.predict(grilla_x.reshape(-1,1))

print(f'Peso especifico estimado del metal: {ajus.coef_[0]}')

errores = data_lyp['peso'] - ajus.predict(data_lyp[['longitud']])
#print(errores)
#plt.hist(errores, bins = 8)
print(f'ECM: {(errores ** 2).mean()}')

data_lyp.plot.scatter('longitud','peso')
plt.title('ajuste lineal usando sklearn')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.show()