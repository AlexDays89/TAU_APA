import os
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.llms.huggingface import HuggingFaceLLM
from transformers import AutoTokenizer, AutoModelForCausalLM

# 0. Rutas
INDEX_DIR = "./index_store/cieo"
LLM_MODEL = "mistralai/Mistral-7B-Instruct-v0.3"

# 1. Configurar modelo LLM
llm = HuggingFaceLLM(
    model_name=LLM_MODEL,
    tokenizer_name=LLM_MODEL,
    context_window=4096,
    max_new_tokens=256,
    generate_kwargs={"temperature": 0.0, "do_sample": False},
    model_kwargs={"load_in_4bit": True, "device_map": "auto"},
)

# 2. Cargar índice
storage_context = StorageContext.from_defaults(persist_dir=INDEX_DIR)
index = load_index_from_storage(storage_context)

# 3. Crear motor de consulta
from llama_index.core.query_engine import RetrieverQueryEngine
query_engine = RetrieverQueryEngine.from_args(index.as_retriever(), llm=llm)

# 4. Loop de preguntas
while True:
    pregunta = input("\n🔎 Pregunta (ENTER para salir): ")
    if not pregunta.strip():
        break
    try:
        respuesta = query_engine.query(pregunta)
        print("\n📘 Respuesta:")
        print(respuesta.response)
        print("\n" + "-" * 40 + "\n")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}\n")
