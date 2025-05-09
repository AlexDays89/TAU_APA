from sqlalchemy import create_engine, Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from transformers import AutoTokenizer, AutoModel
import torch

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/TauApa"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Terminologia(Base):
    __tablename__ = 'terminologias'
    __table_args__ = {'schema': 'tau'}

    id = Column(Integer, primary_key=True)
    sistema = Column(String(50))
    codigo = Column(String(50))
    codigo_topografico = Column(String(20))
    termino_preferido = Column(Text)
    sinonimos = Column(Text)
    definicion = Column(Text)
    traduccion_termino = Column(Text)
    traduccion_sinonimos = Column(Text)
    traduccion_definicion = Column(Text)
    fuente = Column(Text)
    fecha_actualizacion = Column(TIMESTAMP)

class RelacionEquivalente(Base):
    __tablename__ = 'relaciones_equivalentes'
    __table_args__ = {'schema': 'tau'}

    id = Column(Integer, primary_key=True)
    codigo_origen = Column(String(50))
    sistema_origen = Column(String(50))
    codigo_destino = Column(String(50))
    sistema_destino = Column(String(50))
    tipo_equivalencia = Column(String(50))
    descripcion = Column(Text)
    fecha_actualizacion = Column(TIMESTAMP)

def create_tables():
    Base.metadata.create_all(engine)

model_name = "dmis-lab/biobert-base-cased-v1.1"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def obtener_embedding(texto):
    tokens = tokenizer(texto, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**tokens)
    return outputs.last_hidden_state.mean(dim=1)

def buscar_en_tabulado(embedding, texto):
    session = SessionLocal()

    # 1. Búsqueda textual básica primero
    resultado = session.query(Terminologia).filter(
        (Terminologia.termino_preferido.ilike(f"%{texto}%")) |
        (Terminologia.sinonimos.ilike(f"%{texto}%")) |
        (Terminologia.definicion.ilike(f"%{texto}%"))
    ).first()

    if resultado:
        session.close()
        return {
            "codigo": resultado.codigo,
            "codigo_topografico": resultado.codigo_topografico,
            "termino_preferido": resultado.termino_preferido,
            "sistema": resultado.sistema
        }

    # 2. Si falla la búsqueda textual, aplicar lógica con embedding
    resultados = session.query(Terminologia).all()
    mejor_similitud = -1
    mejor_fila = None

    for fila in resultados:
        texto_base = fila.termino_preferido or ""
        tokens = tokenizer(texto_base, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            output = model(**tokens)
        emb = output.last_hidden_state.mean(dim=1)
        similitud = torch.cosine_similarity(embedding, emb).item()

        if similitud > mejor_similitud:
            mejor_similitud = similitud
            mejor_fila = fila

    session.close()
    if mejor_fila:
        return {
            "codigo": mejor_fila.codigo,
            "codigo_topografico": mejor_fila.codigo_topografico,
            "termino_preferido": mejor_fila.termino_preferido,
            "sistema": mejor_fila.sistema
        }
    else:
        return {
            "codigo": "0000/0",
            "codigo_topografico": None,
            "termino_preferido": "Sin coincidencia",
            "sistema": "Desconocido"
        }
