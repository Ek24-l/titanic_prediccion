import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Cargar dataset
data = pd.read_csv('prediction/train.csv')

# Seleccionar características
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
data = data.dropna(subset=features)

# Convertir variables categóricas
data = pd.get_dummies(data, columns=['Sex', 'Embarked'], drop_first=True)

X = data[['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Sex_male', 'Embarked_Q', 'Embarked_S']]
y = data['Survived']

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Guardar modelo
joblib.dump(model, 'prediction/titanic_model.pkl')

print("✅ Modelo entrenado y guardado como titanic_model.pkl")
