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
df = pd.read_csv("raw/immat_vehicule.csv", sep=";", encoding="utf-8")

df.to_sql("raw_immat", engine, if_exists="replace", index=False)
