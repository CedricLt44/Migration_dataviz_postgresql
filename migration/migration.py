import pandas as pd
from sqlalchemy import create_engine

from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer les informations sensibles depuis les variables d'environnement
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# Connexion à PostgreSQL
engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

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

df.to_sql("raw_entretiens", engine, if_exists="replace", index=False)
