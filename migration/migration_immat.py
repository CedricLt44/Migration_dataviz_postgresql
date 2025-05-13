import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Charger le fichier
df = pd.read_csv("raw/immat_vehicule.csv", sep=";", encoding="utf-8")

# Connexion à PostgreSQL
engine = create_engine("postgresql+psycopg2://postgres:CleaThaisMuriel1982@localhost:5432/entretienvehicule")
df.to_sql("raw_immat", engine, if_exists="replace", index=False)
