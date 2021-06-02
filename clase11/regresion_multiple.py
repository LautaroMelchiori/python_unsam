import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
import numpy as np


superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])
antigüedad = [50.0, 5.0, 25.0, 70.0]

data_deptos = pd.DataFrame({'alquiler': alquiler, 'superficie': superficie, 'antigüedad': antigüedad})

X = pd.concat([data_deptos.superficie,data_deptos.antigüedad], axis = 1)

ajuste_deptos = linear_model.LinearRegression()
ajuste_deptos.fit(X,data_deptos.alquiler)

# implementacion manual del metodo .predict() de la clase LinearRegression()
def predecir(modelo, df):
    coefs = modelo.coef_
    b = modelo.intercept_

    def calculate_y(x):
        res = b
        for i, coef in enumerate(coefs):
            res +=  x[i] * coef
        
        return res

    predictions = []
    for _, row in df.iterrows():
        prediction = calculate_y(list(row))
        predictions.append(prediction)

    return np.array(predictions)

predecir(ajuste_deptos, X)
errores = data_deptos.alquiler - (ajuste_deptos.predict(X))
print(errores)
print("ECM:", (errores**2).mean()) # error cuadrático medio

"""
En el modelo creado podemos ver que el coeficiente estimado de la variable de
superficie es 0.18069409, haciendo que el precio y la superficie sean directamente
proporcionales.

Lo contrario sucede con la antiguedad, cuyo coeficiente estimado es -0.01213368,
haciendo que el precio y la antiguedad sean inversamente proporcinales
"""