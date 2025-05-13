import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Charger le fichier
df = pd.read_csv("raw/Data2018_2023.csv", sep=";", encoding="utf-8")
# Nettoyage de la colonne "caost"
df["cost"] = (
    df["cost"]
    .str.replace("€", "", regex=False)        # Retirer le symbole €
    .str.replace(",", ".", regex=False)       # Remplacer les virgules par des points
    .str.replace(" ", "", regex=False)        # Supprimer les espaces
    .str.strip()                              # Supprimer les espaces superflus
    .astype(float)                            # Convertir la colonne en float
)
# Nettoyage de la colonne "date"
df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y", errors="coerce")
# Nettoyage de la colonne "kms"
df['kms'] = (
    df['kms']
    .str.strip()                          # Supprimer les espaces en début/fin
    .str.replace(" ", "", regex=False)    # Supprimer les espaces (séparateurs de milliers)
    .astype(float)                        # Convertir la colonne en float
)
# Connexion à PostgreSQL
engine = create_engine("postgresql+psycopg2://postgres:CleaThaisMuriel1982@localhost:5432/entretienvehicule")
df.to_sql("raw_entretiens", engine, if_exists="replace", index=False)
