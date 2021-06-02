#!/usr/bin/python3
# -*- coding: utf-8-*-

# ejercicio 11.16

from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(3141) # semilla para fijar la aleatoriedad

N = 50

indep_vars = np.random.uniform(size = N, low = 0, high = 10)
r = np.random.normal(size = N, loc = 0.0, scale = 8.0) # residuos
dep_vars = 2*indep_vars**2 + 3*indep_vars + 2 + r # relación cuadrática

x = indep_vars
xc = x ** 2
y = dep_vars

X = np.concatenate((x.reshape(-1,1),xc.reshape(-1,1)),axis=1)

lm = linear_model.LinearRegression()
grilla_x = np.linspace(start = 0, stop = 10, num = 1000)


# REGRESION SIMPLE CON X COMO REGRESOR
######################################
lm.fit(x.reshape(-1, 1), y)

a = lm.coef_[0]
b = lm.intercept_

print('Regresion simple con x como regresor')
print(f'a = {a}, b = {b}')

errores = y - lm.predict(x.reshape(-1,1))
print(f'ECM: {(errores ** 2).mean()}')

grilla_y = a * grilla_x + b
plt.plot(grilla_x, grilla_y, c = 'green', label = 'Regresion simple con x como regresor')


# REGRESION SIMPLE CON X² COMO REGRESOR
#######################################
lm.fit(xc.reshape(-1, 1), y)

a = lm.coef_[0]
b = lm.intercept_

print()
print('Regresion simple con x² como regresor')
print(f'a = {a}, b = {b}')

errores = y - lm.predict(xc.reshape(-1,1))
print(f'ECM: {(errores ** 2).mean()}')

grilla_y = a * (grilla_x**2) + b
plt.plot(grilla_x, grilla_y, c = 'yellow', label = 'Regresion simple con x² como regresor')
print()

# REGRESION  MULTIPLE CON X E X² COMO REGRESORES
################################################
lm.fit(X, y)

a = lm.coef_[1]
b = lm.coef_[0]
c = lm.intercept_

print('Regresion multiple con x y x² como regresores')
print(f'a = {a}, b = {b}, c = {c}')

errores = y - lm.predict(X)
print(f'ECM: {(errores ** 2).mean()}')

grilla_y = a * (grilla_x ** 2) + (b * grilla_x) + c
plt.plot(grilla_x, grilla_y, c = 'red', label = 'Regresion multiple con x y x² como regresores')


plt.scatter(x = x , y = y)

plt.legend()

plt.show()