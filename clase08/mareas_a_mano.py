import matplotlib.pyplot as plt
import os
import pandas as pd

archivo = os.path.join('..', 'Data', 'OBS_SHN_SF-BA.csv')

df = pd.read_csv(archivo, index_col = ['Time'], parse_dates = True)

dh = df['12-25-2014':].copy()

# tiempo que tarda la marea entre ambos puertos (1 hora)
delta_t = -1

dh_sf = dh['H_SF']
dh_ba = dh['H_BA']

# diferencia de los ceros de escala entre ambos puertos
# (y agregamos la diferencia entre la primera y segunda medicion de San Fernando
# para compensar por la hora de desplazamiento)
delta_h = abs(dh_sf.iloc[0] - dh_ba.iloc[0]) - abs(dh_sf.iloc[0] - dh_sf.iloc[1])

pd.DataFrame([dh_sf.shift(delta_t) - delta_h, dh_ba]).T.plot()

plt.show()