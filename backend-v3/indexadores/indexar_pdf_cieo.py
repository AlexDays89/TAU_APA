import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core.node_parser import SentenceSplitter

# 0. Rutas y modelos
PDF_PATH = "./data/CIEO-3.1._ACCESIBLE.pdf"
INDEX_DIR = "./index_store/cieo"
LLM_MODEL = "mistralai/Mistral-7B-Instruct-v0.3"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# 1. Cargar documento PDF como nodos
reader = SimpleDirectoryReader(input_files=[PDF_PATH])
docs = reader.load_data()

# 2. Configurar embeddings
embed_model = HuggingFaceEmbedding(model_name=EMBEDDING_MODEL)

# 3. Configurar modelo LLM
llm = HuggingFaceLLM(
    model_name=LLM_MODEL,
    tokenizer_name=LLM_MODEL,
    context_window=4096,
    max_new_tokens=256,
    generate_kwargs={"temperature": 0.0, "do_sample": False},
    model_kwargs={"load_in_4bit": True, "device_map": "auto"},
)

# 4. Aplicar configuración global
Settings.llm = llm
Settings.embed_model = embed_model
Settings.chunk_size = 512  # <- Esto es importante si otras partes del sistema dependen de este tamaño

# 5. Separar en fragmentos
parser = SentenceSplitter(chunk_size=512, chunk_overlap=64)
chunks = parser.get_nodes_from_documents(docs)

# 6. Construir índice solo si no existe (previene reindexado innecesario)
if not os.path.exists(os.path.join(INDEX_DIR, "docstore.json")):
    index = VectorStoreIndex.from_documents(chunks)
    os.makedirs(INDEX_DIR, exist_ok=True)
    index.storage_context.persist(persist_dir=INDEX_DIR)
    print(f"\n✅ Se indexaron {len(chunks)} fragmentos del manual con capacidades generativas para el pipeline de razonamiento.")
else:
    print("ℹ️ El índice ya existe. No se volvió a construir.")
