
# 🧪 CIEO Codificador v3 (TAU + BioBERT Edition)

Este sistema permite sugerir códigos de clasificación clínica (inicialmente CIE-O 3.2) desde texto libre, utilizando modelos de lenguaje como BioBERT y una base terminológica unificada (TAU) que incluye SNOMED CT y CIE-11.

## 🚀 Cómo levantar el sistema

### 1. Base de datos
Levanta PostgreSQL con Docker:
```bash
docker-compose up postgres
```
Ejecuta el script SQL:
```bash
psql -U cieo_user -d cieo_db -f db-schema-v3.sql
```
Carga datos base si lo deseas:
```bash
psql -U cieo_user -d cieo_db -c "\copy terminologias FROM 'tau_base.csv' CSV HEADER;"
```

### 2. Backend (FastAPI + Transformers)
```bash
cd backend-v3
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 3. Frontend (React)
```bash
cd frontend-v3
npm install
npm run dev
```

## 📍 Endpoints disponibles

- `POST /sugerir-codigo`: recibe texto, retorna sugerencia de código desde TAU.
- `GET /`: mensaje de prueba.

## 📊 Base de datos

- `terminologias`: tabla principal con códigos, traducciones y sinónimos.
- `relaciones_equivalentes`: equivalencias entre códigos (CIE-O, SNOMED, CIE-11).

## 🧠 Arquitectura IA (actual)
1. **BioBERT embeddings**.
2. **Comparación con TAU** (por similitud).
3. **Sugerencia del código más probable**.
4. **Registro de correcciones para fine-tuning**.

## 📌 Roadmap personal como desarrollador clínico-IA

| Etapa | Objetivo |
|-------|----------|
| ✅ MVP 1 | Codificador CIE-O con BioBERT + TAU |
| 🔜 MVP 2 | Integrar SNOMED + equivalencias |
| 🔜 MVP 3 | Carga progresiva de traducciones |
| 🔜 MVP 4 | Dataset de entrenamiento incremental |
| 🔜 MVP 5 | Fine-tuning supervisado propio |
| 🔜 MVP 6 | Agente clínico interactivo con búsqueda semántica |

Tu objetivo no es solo codificar diagnósticos, sino entrenar un sistema que **aprenda contigo**, mejore con cada revisión, y sea capaz de ayudarte a razonar clínicamente.

