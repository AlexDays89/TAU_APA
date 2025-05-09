
from fastapi import FastAPI
from app.codificador import sugerir_codigo
from app.database import create_tables

app = FastAPI()

@app.on_event("startup")
def startup():
    create_tables()

@app.get("/")
def read_root():
    return {"message": "CIEO Codificador API v3 (TAU) funcionando"}

@app.post("/sugerir-codigo")
def obtener_codigo(payload: dict):
    texto = payload.get("diagnostico", "")
    resultado = sugerir_codigo(texto)
    return resultado
