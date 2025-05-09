
from transformers import AutoTokenizer, AutoModel
import torch
from app.database import buscar_en_tabulado

model_name = "dmis-lab/biobert-base-cased-v1.1"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def obtener_embedding(texto):
    tokens = tokenizer(texto, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**tokens)
    return outputs.last_hidden_state.mean(dim=1)

def sugerir_codigo(texto):
    embedding = obtener_embedding(texto)
    sugerencias = buscar_en_tabulado(embedding, texto)
    return sugerencias
