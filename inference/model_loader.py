import joblib

MODEL_PATH = "models/logreg_v1.pkl"

model = None


def load_model():
    global model
    if model is None:
        model = joblib.load(MODEL_PATH)
    return model
