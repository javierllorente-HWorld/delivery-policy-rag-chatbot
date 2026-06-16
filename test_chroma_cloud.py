import chromadb

print("Conectando a Chroma Cloud")

client = chromadb.CloudClient(
    api_key="ck-6HbuPgtt1zi3ersMP5DuA3oY659ZdAKZiCSW79dWyELT",
    tenant="639f121d-09f8-4150-bfe5-7348282691e9",
    database="delivery_policy_rag"
)

print("Cliente OK")

collection = client.get_or_create_collection(
    name="delivery_policies_v1",
    embedding_function=None
)

print("Colección OK")


print("OK")
from sentence_transformers import SentenceTransformer

print("Cargando modelo")

model = SentenceTransformer("all-MiniLM-L6-v2")

docs = [
    "El delivery tarda entre 30 y 45 minutos.",
    "Si el pedido llega frío, el cliente puede reclamar reembolso parcial.",
    "El repartidor debe confirmar la entrega en la app."
]

embeddings = model.encode(docs).tolist()

collection.add(
    ids=["policy_201", "policy_202", "policy_203"],
    documents=docs,
    embeddings=embeddings
)

print("OK embeddings reales")

query = "¿Qué pasa si el pedido llega frío?"

query_embedding = model.encode([query]).tolist()[0]

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)

print(results["documents"])