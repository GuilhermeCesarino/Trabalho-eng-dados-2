import pandas as pd
import pyodbc
from minio import Minio
import os
from datetime import datetime

# conexão SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=.\\SQLEXPRESS;"
    "DATABASE=NetflixDB;"
    "Trusted_Connection=yes;"
)

# MinIO
client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

bucket_name = "landing-zone"

if not client.bucket_exists(bucket_name):
    client.make_bucket(bucket_name)

tabelas = [
    "Conteudo",
    "Ator",
    "Diretor",
    "Pais",
    "Genero",
    "Conteudo_Ator",
    "Conteudo_Diretor",
    "Conteudo_Pais",
    "Conteudo_Genero"
]

os.makedirs("C:/temp", exist_ok=True)

data = datetime.now().strftime("%Y-%m-%d")

for tabela in tabelas:
    print(f"Exportando {tabela}...")

    df = pd.read_sql(f"SELECT * FROM {tabela}", conn)

    arquivo = f"{tabela}_{data}.csv"
    caminho = f"C:/temp/{arquivo}"

    df.to_csv(caminho, index=False, encoding="utf-8-sig")

    client.fput_object(
        bucket_name,
        arquivo,
        caminho
    )

    print(f"{tabela} enviado!")

conn.close()

print("✅ Tudo exportado para o MinIO!")