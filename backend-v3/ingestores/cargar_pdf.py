import fitz  # PyMuPDF
from config import DATA_DIR

def procesar_pdf(ruta_pdf):
    doc = fitz.open(ruta_pdf)
    fragmentos = []
    for i, page in enumerate(doc):
        texto = page.get_text()
        if texto.strip():
            fragmentos.append({
                "pagina": i + 1,
                "texto": texto
            })

    # Aquí puedes guardar a disco o base para luego ser indexado por Haystack
    print(f"📄 PDF procesado: {len(fragmentos)} fragmentos extraídos")

    # (Opcional) guardar JSON o insertar en tabla `documentos_fragmentos`