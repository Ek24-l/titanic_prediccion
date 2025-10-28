from django.http import JsonResponse
import joblib
import numpy as np
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# Cargar el modelo entrenado
model = joblib.load('prediction/titanic_model.pkl')

@csrf_exempt
def predict_survival(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # Convertir los datos a los nombres que tu modelo espera
        Pclass = int(data.get('pclass', 3))
        Age = float(data.get('age', 30))
        SibSp = int(data.get('sibsp', 0))
        Parch = int(data.get('parch', 0))
        # Fare, Sex_male, Embarked_Q, Embarked_S puedes definir valores por defecto o calcular
        Fare = float(data.get('fare', 30))
        Sex_male = 1 if data.get('sex', 'male') == 'male' else 0
        Embarked_Q = int(data.get('embarked_q', 0))
        Embarked_S = int(data.get('embarked_s', 1))

        features = np.array([[Pclass, Age, SibSp, Parch, Fare, Sex_male, Embarked_Q, Embarked_S]])
        prediction = int(model.predict(features)[0])
        probability = float(model.predict_proba(features)[0][1])  # probabilidad de sobrevivir

        return JsonResponse({'prediction': prediction, 'probability': probability})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
