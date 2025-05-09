import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
from config import DATABASE_URL, COLUMNAS_TERMINOLOGIA, SCHEMA_NAME

def procesar_excel(ruta_excel):
    df = pd.read_excel(ruta_excel)

    # 🧠 Detectar tipo de Excel por columnas clave
    if "ICD-O Morphology Code" in df.columns and "Preferred Term" in df.columns:
        # Normalización de columnas
        df = df.rename(columns={
            "ICD-O Morphology Code": "codigo",
            "Preferred Term": "termino_preferido"
        })
        df["sistema"] = "CIE-O"
        df["fuente"] = "Histology"
        df["codigo_topografico"] = None
        df["sinonimos"] = None
        df["definicion"] = None
        df["traduccion_termino"] = None
        df["traduccion_sinonimos"] = None
        df["traduccion_definicion"] = None
        df["fecha_actualizacion"] = datetime.now()

        # Asegurar columnas correctas y ordenadas
        df = df[COLUMNAS_TERMINOLOGIA]

        # Insertar en base de datos
        engine = create_engine(DATABASE_URL)
        df.to_sql("terminologias", engine, schema=SCHEMA_NAME, if_exists="append", index=False)
        print("✅ Histology ICD-O cargado correctamente.")
    else:
        print("⚠️ Formato de Excel no reconocido como tabla ICD-O válida.")

