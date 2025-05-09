from pathlib import Path

# 📁 Rutas principales
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "modelos"
DEFAULT_MODEL_PATH = MODELS_DIR / "biobert-base-cased-v1.1"

# 🛢️ Configuración de base de datos
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/TauApa"
SCHEMA_NAME = "tau"

# 📊 Configuración de columnas comunes
COLUMNAS_TERMINOLOGIA = [
    "sistema", "codigo", "codigo_topografico", "termino_preferido",
    "sinonimos", "definicion", "traduccion_termino", "traduccion_sinonimos",
    "traduccion_definicion", "fuente", "fecha_actualizacion"
]