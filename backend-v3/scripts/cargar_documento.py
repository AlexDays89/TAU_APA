import sys
from pathlib import Path

# Importamos configuración y adaptadores
from config import DATA_DIR
from ingestores import cargar_excel, cargar_pdf

def main(ruta_archivo):
    ruta = Path(ruta_archivo)
    if not ruta.exists():
        print(f"❌ Archivo no encontrado: {ruta}")
        return

    if ruta.suffix in [".xlsx", ".xls"]:
        cargar_excel.procesar_excel(ruta)
    elif ruta.suffix in [".pdf"]:
        cargar_pdf.procesar_pdf(ruta)
    else:
        print(f"⚠️ Formato no soportado: {ruta.suffix}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python cargar_documento.py archivo.ext")
    else:
        main(sys.argv[1])