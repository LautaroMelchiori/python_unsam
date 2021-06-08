# ejercicio 12.12

from copy import deepcopy
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

iris_dataset = load_iris()


def comparar_modelos(modelos, nombres, n_experimentos):
    """
    Recibe una lista 'modelos' de modelos, y una lista 
    'nombres' de strings con los nombres de los mismos, 
    y un numero entero 'n_experimentos', con la cantidad 
    de experimentos a realizar

    Pre: len(modelos) == len(nombres)

    Devuelve un diccionario donde las claves son los nombres de cada 
    modelo y los valores son el promedio de los scores de los mismos
    clasificando datos de el data set de flores Iris
    """
    # deepcopiamos los modelos para no modificar
    # los que son entregados como parametros
    models = deepcopy(modelos)

    # diccionario con listas donde guardaremos los scores
    scores = {}
    for nombre in nombres:
        scores[nombre] = []

    for _ in range(n_experimentos):
        # spliteamos datos
        X_train, X_test, y_train, y_test = train_test_split(
            iris_dataset['data'], iris_dataset['target'])

        # zona de entrenamiento
        for i, model in enumerate(models):
            model.fit(X_train, y_train)
            score = model.score(X_test, y_test)
            scores[nombres[i]].append(score)

    # calculamos los promedios
    for score in scores:
        scores[score] = np.mean(scores[score])

    return scores


# declaracion de modelos
knn = KNeighborsClassifier(n_neighbors=1)
clf = DecisionTreeClassifier()
rf = RandomForestClassifier()

modelos = [knn, clf, rf]
nombres = ['Knn', 'Decision Tree', 'Random Forest']
n = 100

resultados = comparar_modelos(modelos, nombres, n)

# imprimimos los resultados
for nombre, promedio in resultados.items():
    print(f'Score promedio {nombre}: {promedio:.2f}')
