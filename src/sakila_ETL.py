# src/sakila_etl.py
# Proceso ETL para base de datos Sakila
# Arquitectura: cada consulta SQL vive en queries/*.sql
# Python solo orquesta: conecta, ejecuta, guarda CSV.

import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path
import os
from config import *

# Carpeta de queries relativa a la raíz del proyecto
QUERIES_DIR = Path(__file__).parent.parent / 'queries'

# Mapeo: nombre_de_archivo_sql → nombre_de_archivo_csv
# Modelo estrella: 1 tabla de hechos + 5 dimensiones
CONSULTAS = {
    'Dataframe_1_Clientes.sql':          'Dataframe_1_Clientes.csv',
    'Dataframe_2_CatalogoPeliculas.sql': 'Dataframe_2_CatalogoPeliculas.csv',
    'Dataframe_3_Elenco_Popularidad.sql':'Dataframe_3_Elenco_Popularidad.csv',
    'Dataframe_4_amount.sql':            'Dataframe_4_amount.csv',
}

def conectar_bd():
    url = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    engine = create_engine(url)
    return engine

def extraer_datos(engine):
    resultados = {}
    for archivo_sql, archivo_csv in CONSULTAS.items():
        ruta_sql = QUERIES_DIR / archivo_sql
        query = ruta_sql.read_text(encoding='utf-8')
        df = pd.read_sql(query, engine)
        resultados[archivo_csv] = df
    return resultados

def guardar_archivos(resultados):
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    for archivo_csv, df in resultados.items():
        df.to_csv(f'{OUTPUT_FOLDER}/{archivo_csv}', index=False)

def proceso_completo():
    try:
        engine = conectar_bd()
        resultados = extraer_datos(engine)
        guardar_archivos(resultados)
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    proceso_completo()