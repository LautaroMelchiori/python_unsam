# ejercicio 12.11

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

iris_dataset = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'])

knn = KNeighborsClassifier(n_neighbors=1)
clf = DecisionTreeClassifier()

knn.fit(X_train, y_train)
clf.fit(X_train, y_train)

print(f'Knn score: {knn.score(X_test, y_test):.2f}')
print(f'Decision tree score: {clf.score(X_test, y_test):.2f}')
