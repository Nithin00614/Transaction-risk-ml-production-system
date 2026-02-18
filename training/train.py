import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
import joblib

from features import load_and_prepare_data


def train():
    X, y = load_and_prepare_data("data/raw/transactions.csv")

    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=1000)

    with mlflow.start_run():
        model.fit(X_train, y_train)

        preds = model.predict_proba(X_val)[:, 1]
        auc = roc_auc_score(y_val, preds)

        mlflow.log_metric("roc_auc", auc)
        mlflow.sklearn.log_model(model, "model")

        print(f"ROC-AUC: {auc:.4f}")

    joblib.dump(model, "models/model.pkl")


if __name__ == "__main__":
    train()
