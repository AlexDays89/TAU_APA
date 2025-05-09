
# 🛠️ CIEO Codificador — README para desarrolladores

Este proyecto es un codificador clínico inteligente, diseñado para mapear diagnósticos en texto libre a códigos normalizados como CIE-O, SNOMED CT y CIE-11.

## 🧱 Componentes principales

- **Frontend (React)**: pestañas por nomenclatura, con visor editable por código.
- **Backend (FastAPI + Transformers)**: motor de sugerencias y gestión de equivalencias.
- **Modelo IA**: BioBERT (`dmis-lab/biobert-base-cased-v1.1`), usado para vectorizar texto libre.
- **Base de datos (PostgreSQL)**: esquema terminológico unificado (TAU).

## 🧩 Estructura de TAU (Terminológico APA Unificado)

Tabla `terminologias`:

| Campo | Uso |
|-------|-----|
| sistema | CIE-O, SNOMED, CIE-11 |
| codigo | Código oficial |
| termino_preferido | Término base |
| sinonimos | Lista separada por `;` |
| definicion | Descripción base |
| traduccion_* | Campos editables |
| fuente | Origen del código |

Tabla `relaciones_equivalentes`:

Permite mapear entre códigos (ej: `8500/3` = `254837009`), útil para interoperabilidad y aprendizaje cruzado.

## 🧪 Objetivo técnico

- Desacoplar el modelo de la nomenclatura (cualquier código puede integrarse).
- Permitir entrenamiento incremental y compartido.
- Soporte futuro para RAG (retrieval-augmented generation).

## 🔁 Extensión sugerida

- Agregar árbol jerárquico (SNOMED) para navegación.
- Crear dataset exportable para HuggingFace Trainer.
- Agregar autenticación para trazabilidad de sugerencias por usuario.

## 🤝 Contribución

Este proyecto está pensado para crecer. Si encuentras una forma de:
- Mejorar sugerencias.
- Integrar más estándares.
- O expandir el frontend.

¡Eres bienvenido a proponer y construir!

