import numpy as np
import matplotlib.pyplot as plt

temperaturas = np.load("../Data/Temperaturas.npy")

plt.hist(temperaturas, bins = 20)
plt.xlabel("Medición de temperatura (grados)")
plt.ylabel("Mediciones")
plt.title("Mediciones de una temperatura de 37.5° con error gaussiano")
plt.show()