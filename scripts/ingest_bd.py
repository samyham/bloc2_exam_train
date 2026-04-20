import pandas as pd
from sqlalchemy import create_engine

# Connexion PostgreSQL
engine = create_engine("postgresql://user:password@localhost:5432/rncp_db")

# Charger le dataset
df = pd.read_csv("data/processed/fact_stock_risk.csv")

# Envoyer en base
df.to_sql("fact_stock_risk", engine, if_exists="replace", index=False)

print("Données insérées dans PostgreSQL")