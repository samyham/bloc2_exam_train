# 📦 Projet Data Engineering & Machine Learning

## 🎯 Objectif

Ce projet a pour objectif de construire un pipeline complet de traitement de données permettant :

- l’ingestion de données hétérogènes (CSV, JSON, JSONL)
- leur transformation et nettoyage (ETL)
- la création d’une table analytique
- l’entraînement d’un modèle de machine learning
- le stockage des données dans PostgreSQL via Docker

---

## 🧱 Architecture du projet

bloc2_project/
│
├── data/
│ ├── raw/
│ └── processed/
│
├── scripts/
│ ├── ingest.py
│ ├── etl.py
│ ├── train.py
│ ├── ingest_db.py
│
├── models/
│ └── model.pkl
│
├── sql/
│ ├── schema.sql
│ └── queries.sql
│
├── docker-compose.yml
└── README.md

---

## ⚙️ Pipeline

### 1. Ingestion

Chargement des données depuis différentes sources :

- CSV : orders, products, stores
- JSON : inventory
- JSONL : reviews

---

### 2. ETL

- nettoyage des données
- gestion des valeurs manquantes
- agrégation des ventes (7j / 30j)
- jointures entre datasets

Création de la table :

👉 `fact_stock_risk`

---

### 3. Machine Learning

- Modèle : RandomForestClassifier
- Objectif : prédire `stockout_risk`

⚠️ Attention : dataset simple → score élevé à interpréter avec prudence

---

### 4. Stockage

- Base PostgreSQL via Docker
- Insertion avec SQLAlchemy

---

## ▶️ Exécution

```bash
python scripts/ingest.py
python scripts/etl.py
python scripts/train.py
python scripts/ingest_db.py
📊 Résultats
Dataset final : fact_stock_risk.csv
Modèle : model.pkl
Données stockées dans PostgreSQL

🧠 Conclusion

Ce projet met en place un pipeline complet de data engineering, depuis l’ingestion jusqu’au stockage en base, avec une première approche de machine learning.
