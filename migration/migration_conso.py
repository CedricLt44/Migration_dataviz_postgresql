import pandas as pd
import psycopg2
from sqlalchemy import create_engine

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

# Connexion à PostgreSQL
engine = create_engine("postgresql+psycopg2://postgres:CleaThaisMuriel1982@localhost:5432/entretienvehicule")
df.to_sql("raw_conso", engine, if_exists="replace", index=False)
