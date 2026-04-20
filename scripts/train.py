import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# =========================
# PATH
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

DATA_PATH = os.path.join(PROJECT_DIR, "data", "processed", "fact_stock_risk.csv")
MODEL_PATH = os.path.join(PROJECT_DIR, "models", "model.pkl")

os.makedirs(os.path.join(PROJECT_DIR, "models"), exist_ok=True)

# =========================
# LOAD DATA
# =========================
def load_data():
    return pd.read_csv(DATA_PATH)

# =========================
# PREPARE DATA
# =========================
def prepare_data(df):

    X = df.drop(columns=["stockout_risk"])
    y = df["stockout_risk"]

    # Encodage des variables catégorielles
    for col in X.select_dtypes(include=["object"]).columns:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))

    return X, y

# =========================
# TRAIN MODEL
# =========================
def train_model(X_train, y_train):
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model

# =========================
# EVALUATE
# =========================
def evaluate(model, X_test, y_test):
    y_pred = model.predict(X_test)

    print("\n=== EVALUATION ===")
    print("Accuracy :", accuracy_score(y_test, y_pred))
    print("\nClassification report :")
    print(classification_report(y_test, y_pred))

# =========================
# SAVE MODEL
# =========================
def save_model(model):
    joblib.dump(model, MODEL_PATH)
    print("\nModèle sauvegardé :", MODEL_PATH)

# =========================
# RUN
# =========================
if __name__ == "__main__":

    df = load_data()

    print("Shape dataset :", df.shape)

    X, y = prepare_data(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = train_model(X_train, y_train)

    evaluate(model, X_test, y_test)

    save_model(model)