

---

# 🔄 Flujo Inteligente del Ecosistema IA Clínica APA

## 1. 📝 Ingreso del diagnóstico (Frontend)
- Usuario escribe diagnóstico o comentario libre.
- Se envía al Codificador para normalización.

## 2. 🧠 Codificador (BioBERT + TAU)
- Transforma el texto a embeddings con BioBERT.
- Busca coincidencias en la TAU.
- Devuelve sugerencias codificadas por sistema:
  - CIE-O
  - SNOMED CT
  - CIE-11

## 3. 🖥️ Frontend con pestañas + floater
- Muestra sugerencias separadas por sistema.
- Floater permite:
  - Editar traducción.
  - Añadir sinónimos.
  - Ver ruta semántica.
  - Confirmar o rechazar.

## 4. 🔁 Cross Learning Layer
- Si se acepta o edita una sugerencia:
  - Se registra para entrenamiento del codificador.
  - Se actualiza contexto del agente generativo.
- **No se aplica directamente** → pasa a revisión.

## 5. 🧑‍⚖️ Validación / Auditoría (Master Pathologist)
- Casos con override (conflicto o falta de marcadores) se marcan "en revisión".
- El Master valida o rechaza cada aporte al sistema.
- Solo lo validado entrena futuros modelos.

## 6. 🤖 Agente Generativo (RAG + GPT)
- Usa el TAU como base semántica.
- Consulta documentos, papers y normas (RAG).
- Autocompleta informes o responde preguntas clínicas.
- Aprende de lo que el Codificador valida y viceversa.

## ⚠️ Seguridad
| Situación | Acción |
|----------|--------|
| Diagnóstico sin IHQ mínimas | Advierte y ofrece override |
| Codificación sin revisión | No se entrena aún |
| Cambios TAU | Revisión obligatoria |
| Override | Revisión por Master Pathologist |

---

Este flujo asegura que el sistema:
- Aprende de forma segura.
- No replica errores.
- Puede escalar como una IA de apoyo clínico verificada y auditable.

