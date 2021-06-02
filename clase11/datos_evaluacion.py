#!/usr/bin/python3
# -*- coding: utf-8-*-

# ejercicio 11.19

# PARA GRAFICAR
#import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

def pot(x,n):
    """
    Recibe un array 'x' y un numero 'n'
    
    Devuelve una matriz de shape(len(x), n)
    conteniendo los valores de las primeras n potencias de x 
    """
    X=x.reshape(-1,1)
    for i in range(n-1):
        X=np.concatenate((X,(x**(i+2)).reshape(-1,1)),axis=1)
    return X

def AIC(k, ecm, num_params):
    '''
    Calcula el AIC de una regresión lineal múltiple de 'num_params'
    parámetros, ajustada sobre una muestra de 'k' elementos, y que da 
    lugar a un error cuadrático medio 'ecm'.
    '''
    aic = k * np.log(ecm) + 2 * num_params
    return aic

np.random.seed(3141) # semilla para fijar la aleatoriedad

N = 50

# generamos los datos de entrenamiento
indep_vars = np.random.uniform(size = N, low = 0, high = 10)
r = np.random.normal(size = N, loc = 0.0, scale = 8.0) # residuos
dep_vars = 2*indep_vars**2 + 3*indep_vars + 2 + r # relación cuadrática

x = indep_vars
y = dep_vars

#genero datos para evaluar 
x_test = np.random.uniform(size = N, low = 0, high = 10) 
r_test = np.random.normal(size = N, loc = 0.0, scale = 8.0) # residuos
y_test = 2*x_test**2 + 3*x_test + 2 + r_test # misma relación cuadrática

# Modelo de regresion linear que usaremos para los calculos
lm = linear_model.LinearRegression()

# PARA GRAFICAR
#grilla_x = np.linspace(start = 0, stop = 10, num = 1000)

# lista donde guardaremos el valor AIC de cada modelo
aics = []

# Calcularemos el ECM y el AIC de distintos modelos polinomiales
# para la relacion cuadratica descrita arriba
for i in range(1, 12):
    # generamos una matriz con las variables explicativas
    # que seran las primeras i potencias de x
    x_training = pot(x, i)

    # ajustamos el modelo
    lm.fit(x_training, y)
    
    # calculamos ecm y aic a parttir de un data set fresco, de evaluacion
    # (lo normalizamos pasandolo por la funcion 'pot' para que tenga la misma
    # forma que el data set de entrenamiento)
    errores = y_test - lm.predict(pot(x_test, i))
    ecm = (errores ** 2).mean()
    grado = i
    num_params = grado + 1
    aic = AIC(len(x_training), ecm, num_params)
    aics.append(aic)

    print('------------------------------')
    print(f'Grado del polinomio: {grado}')
    #print(f'Cantidad de parametros: {num_params}')
    print(f'ECM: {ecm}')
    #print(f'AIC: {aic}')

    # PARA GRAFICAR
    #grilla_y = lm.intercept_

    #for i, coef in enumerate(lm.coef_):
    #    grilla_y += (grilla_x ** (i + 1)) * coef

    #plt.plot(grilla_x, grilla_y, label = f'Mod. polinomial grado {grado}')

# PARA GRAFICAR
#plt.scatter(x_test, y_test)
#plt.legend()
#plt.show()

print()
print(f'El modelo polinomial que mas minimiza el AIC es el de grado {np.argmin(aics) + 1}')