import os
import pandas as pd
from sqlalchemy import create_engine

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

# Connexion
engine = create_engine("postgresql://user:password@localhost:5432/rncp_db")

# Bon chemin
file_path = os.path.join(PROJECT_DIR, "data", "processed", "fact_stock_risk.csv")

df = pd.read_csv(file_path)

df.to_sql("fact_stock_risk", engine, if_exists="replace", index=False)

print("Données insérées dans PostgreSQL")
