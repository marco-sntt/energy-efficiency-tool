import joblib
import pandas as pd
import os

# Carica i modelli
model_dir = os.path.join(os.path.dirname(__file__), '..', 'models')
models = {
    i: joblib.load(os.path.join(model_dir, f"XGBoost_{i}.pkl")) for i in range(1, 7)
}

def predizione_intervento(input_data):
    categoria = input_data.pop("CATEGORIA_INTERVENTO", None)
    if categoria not in models:
        raise ValueError(f"Categoria di intervento {categoria} non valida. Deve essere un intero tra 1 e 6.")
    X_input = pd.DataFrame([input_data])
    modello = models[categoria]
    predizione = modello.predict(X_input)
    return predizione[0]
