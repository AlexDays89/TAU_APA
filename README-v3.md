
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

🧠 Objetivo: Construir la mejor IA gratuita para codificación médica, con base en CIE-O, SNOMED y documentos clínicos.
🔩 1. Modelo base (IA generativa / comprensiva)
Componente	Rol	Modelo recomendado	¿Por qué?
🧠 LLM principal	Entender PDFs, responder preguntas, asistir diagnóstico	Mistral o Phi-2	Gratuitos, eficientes y potentes
🔍 Indexador documental	Convertir PDFs en conocimiento consultable	LlamaIndex o Haystack	Ideal para RAG con libros/manuales
📚 Embeddings	Búsqueda semántica	InstructorEmbedding o GTE-base	Gratuitos y multiuso

📊 2. Codificador médico (semántico y estructurado)
Componente	Rol	Modelo recomendado	¿Por qué?
🧬 Codificador clínico	Embedding de términos médicos	BioBERT	Optimizado para lenguaje biomédico
🧮 Comparador semántico	Buscar el código más cercano	Distancia coseno con FAISS	Ultra rápido y gratuito
🧰 Sistema de entrenamiento	Fine-tuning del modelo	PyTorch + HuggingFace	Gratuito y bien documentado

💾 3. Base de datos médica curada (TAU)
Ya lo tienes con:

terminologias (estructura común)

relaciones_equivalentes (cruces SNOMED/CIE-11)

Posibilidad de importar de Excel/PDF/API

🖥️ 4. Requisitos de hardware
Nivel	RAM	GPU recomendada	¿Permite qué?
Básico	16 GB	Ninguna	Ingesta + embeddings + consultas
Medio	32 GB	RTX 3060-3070	LLM de 7B en CPU o GPU lenta
Avanzado	64 GB	RTX 4090 o A6000	Entrenar modelos, codificador + generativo en paralelo

🔄 5. Interacción y entrenamiento
Podrás:

Entrenar desde texto libre.

Agregar nuevas fuentes (PDFs, libros, artículos).

Crear sinónimos, traducciones y equivalencias.

Rastrear quién entrenó qué (auditoría médica).

Conectarlo luego a tu sistema LIS de APA.

---

🧠 Resumen del avance - Entrenamiento e Indexación IA CIE-O
📁 Estructura de Proyecto Establecida
java
Copiar
Editar
TAU_APA/
├── backend-v3/
│   ├── data/                        ← Documentos fuente como CIE-O 3.1 PDF
│   ├── index_store/cieo/           ← Índice persistente de vectores (vector DB)
│   ├── indexadores/
│   │   └── indexar_pdf_cieo.py     ← Script de indexación inteligente con LLM
│   ├── Consultar Rag Cieo.py       ← Script de consulta interactiva (RAG)
✅ Objetivo de hoy
Construir una IA capaz de comprender y razonar sobre el manual CIE-O 3.1 en español, para utilizarlo como base de conocimiento médico en codificación oncológica.

⚙️ Pipeline completado
📚 Ingesta e Indexación de CIE-O PDF

Cargamos el manual como SimpleDirectoryReader

Lo dividimos en fragmentos con SentenceSplitter

Creamos embeddings con all-MiniLM-L6-v2

Integramos un LLM local (Mistral-7B-Instruct-v0.3)

Se guardó el índice vectorial en index_store/cieo

🤖 Consulta basada en recuperación (RAG)

Se configuró un RetrieverQueryEngine conectado al índice

Permite consultar conceptos desde terminal con respuestas contextuales generadas por el LLM

🔐 Autenticación Hugging Face

Se solucionaron problemas de token y autenticación

El modelo Mistral fue correctamente accedido con login persistente

💡 Ideas clave del diseño
El índice vectorial será usado por un agente más complejo en etapas futuras

El modelo debe sugerir códigos, explicar decisiones y aprender de correcciones

El entrenamiento se basa en ingestión progresiva de documentos normativos (CIE-O, CAP, SNOMED, etc.)

Se prevé una interfaz web y conexión con el frontend en React

🛠️ Próximos pasos sugeridos
🧪 Verificar la calidad de los chunks indexados (contenido, longitud, metadatos)

🧠 Entrenar al modelo con consultas clave para testear razonamiento

📄 Agregar más documentos (p. ej., tablas SNOMED, CIE-11)

🔄 Interfaz de consulta desde frontend (formulario, respuestas enriquecidas)

🧬 Futuro: codificador contextual que lea el diagnóstico completo y determine código morfológico + topográfico.

---

🧠 PIPELINE MAESTRO DE INDEXACIÓN Y RAZONAMIENTO – CIE-O
🎯 Objetivo General
Construir un sistema de IA local que permita sugerir, validar y razonar codificaciones médicas (inicialmente CIE-O 3.1) desde texto libre, con generación explicativa, trazabilidad de fuentes y entrenamiento continuo desde el frontend.

🧱 1. Indexación Semántica + Generativa
Script principal: indexar_pdf_cieo.py

Fuente: CIEO-3.1._ACCESIBLE.pdf (manual en español)

Procesos:

Carga del PDF y fragmentación inteligente con SentenceSplitter

Vectorización semántica con all-MiniLM-L6-v2

Carga de modelo generativo Mistral-7B-Instruct-v0.3 para razonamiento explicativo

Almacenamiento en ./index_store/cieo con persistencia en disco

✅ Indexa 700 fragmentos del manual con chunking consistente

🧪 2. Motor de Consulta RAG (Retrieval-Augmented Generation)
Script: consultar_rag_cieo.py

Módulo: RetrieverQueryEngine de LlamaIndex

Entrada: Preguntas en lenguaje natural desde terminal

Salida: Texto generado por el LLM, usando los fragmentos indexados como respaldo.

Soporte a futuro:

Añadir referencias visibles al fragmento fuente (para validación clínica)

Añadir modo rápido vs explicativo (para performance clínica vs docencia)

🔄 3. Normalización y Expansión Terminológica
Base: terminologias (TAU)

Fuentes previstas:

Excel de morfología v26

SNOMED CT (por API o dumps)

CIE-11

Flujo esperado:

Scripts de carga flexibles por formato (ingestores/)

Reconocimiento automático de columnas

Curación automática + revisión humana

Modo sugerencia con IA desde texto libre + embeddings

🤖 4. Futuro Agente Diagnóstico (Copiloto Médico)
Lectura completa del informe

Detección de entidades: lateralidad, grado, topografía

Interacción tipo chat con explicación y sugerencia de codificación

Posibilidad de autocompletar sinónimos, correcciones ortográficas y terminologías vinculadas

Flujo de entrenamiento activo desde la UI (aceptar/sugerir/editar código = feedback al modelo)

🌐 5. Interfaz Web (frontend)
Webapp en React (futura etapa)

Entrada del texto libre de diagnóstico

Sugerencias de código automáticas con botones de:

🔍 "Buscar en manual"

🧠 "Razonar con IA"

🔄 "Consultar SNOMED" / "Consultar CIE-11"

Validación cruzada de respuestas (p. ej. comparar CIE-O vs SNOMED)

📌 6. Trazabilidad, Fine-tuning y Memoria
Cada sugerencia aceptada:

Se registra para refinar embeddings

Actualiza sinónimos, definiciones o nuevas relaciones

Opcional: puede nutrir el entrenamiento de un modelo propio

Todos los cambios deben trazarse por usuario, tiempo y origen

🔧 Requerimientos técnicos actuales
✅ Funciona localmente en:

ASUS Zephyrus G16

Intel Core Ultra i9

32 GB RAM

GPU RTX 4070

⚠️ Consideraciones para escalar
Requisito	Estado Actual	Recomendación para IA Rápida
RAM	32 GB	Suficiente para modelos 7B
GPU VRAM	8 GB+	Ideal: 24 GB para tuning / 16 GB para inferencia
Disco SSD	1 TB NVMe	OK
CPU	Intel Ultra i9	OK, pero el cuello de botella será la GPU
Sistema dedicado (headless)	❌	🤔 Considerar torre con refrigeración activa