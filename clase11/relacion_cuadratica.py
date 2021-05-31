import matplotlib.pyplot as plt
import numpy as np

def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

np.random.seed(3141) # semilla para fijar la aleatoriedad

N = 50

indep_vars = np.random.uniform(size = N, low = 0, high = 10)
r = np.random.normal(size = N, loc = 0.0, scale = 8.0) # residuos
dep_vars = 2 + 3*indep_vars + 2*indep_vars**2 + r # relación cuadrática

x = indep_vars
y = dep_vars

a, b = ajuste_lineal_simple(x, y)

errores = y - (x*a + b)
print("ECM", (errores**2).mean())

grilla_x = np.linspace(start = 0, stop = 10, num = 1000)
grilla_y = grilla_x*a + b

plt.scatter(x = x , y = y)
plt.plot(grilla_x, grilla_y, c = 'green')

plt.title('ajuste lineal')
plt.show()