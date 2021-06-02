#!/usr/bin/python3
# -*- coding: utf-8-*-

# ejercicio 11.17

from sklearn import linear_model
import numpy as np
#import matplotlib.pyplot as plt

np.random.seed(3141) # semilla para fijar la aleatoriedad

N = 50

indep_vars = np.random.uniform(size = N, low = 0, high = 10)
r = np.random.normal(size = N, loc = 0.0, scale = 8.0) # residuos
dep_vars = 2*indep_vars**2 + 3*indep_vars + 2 + r # relación cuadrática

x = indep_vars
y = dep_vars

def pot(x,n):
    X=x.reshape(-1,1)
    for i in range(n-1):
        X=np.concatenate((X,(x**(i+2)).reshape(-1,1)),axis=1)
    return X

lm = linear_model.LinearRegression()

# para graficar
#grilla_x = np.linspace(start = 0, stop = 10, num = 1000)

for i in range(1, 9):
    X = pot(x, i)

    lm.fit(X, y)
    
    errores = y - lm.predict(X)

    print('------------------------------')
    print(f'Grado del polinomio: {i}')
    print(f'Cantidad de parametros: {i + 1}')
    print(f'ECM: {(errores ** 2).mean()}')

    # graficar    
    #grilla_y = lm.intercept_

    #for i, coef in enumerate(lm.coef_):
    #    grilla_y += (grilla_x ** (i + 1)) * coef

    #plt.plot(grilla_x, grilla_y, label = f'{i}')

#plt.scatter(x, y)
#plt.legend()
#plt.show()