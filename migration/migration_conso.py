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
df = pd.read_csv("raw/conso.csv", sep=";", encoding="utf-8")

# convertion colonne "date"
df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y", errors="coerce")

# Nettoyage"
df['immat'] = (
    df['immat']
    .str.strip()                          # Supprimer les espaces en début/fin
)

df["Score_Heure"] = (
    df["Score_Heure"]
    .str.replace(",", ".", regex=False)       # Remplacer les virgules par des points
    .str.replace(" ", "", regex=False)        # Supprimer les espaces
    .str.strip()                              # Supprimer les espaces superflus
    .astype(float)                            # Convertir la colonne en float
)
df["Distance"] = (
    df["Distance"]
    .str.replace(",", ".", regex=False)       # Remplacer les virgules par des points
    .str.replace(" ", "", regex=False)        # Supprimer les espaces
    .str.strip()                              # Supprimer les espaces superflus
    .astype(float)                            # Convertir la colonne en float
)

df["conso"] = (
    df["conso"]
    .str.replace(",", ".", regex=False)       # Remplacer les virgules par des points
    .str.replace(" ", "", regex=False)        # Supprimer les espaces
    .str.strip()                              # Supprimer les espaces superflus
    .astype(float)                            # Convertir la colonne en float
)

# Conversion des colonnes en nombres entiers
colonnes = ["Vitesse", "Frein_brusques", "Acc_brusques", "Virages_brusques", "Surregime", "Total_points"]
df[colonnes] = df[colonnes].fillna(0).astype(int)

df.to_sql("raw_conso", engine, if_exists="replace", index=False)
