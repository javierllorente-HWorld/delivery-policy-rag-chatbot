import chromadb
from sentence_transformers import SentenceTransformer

print("Inicio")

client = chromadb.CloudClient(
    api_key='ck-5BPvPtLez1sKCBrYRewW4Rf9cbYTx5jj3jMp865HA2no',
    tenant="639f121d-09f8-4150-bfe5-7348282691e9",
    database="delivery_policy_rag"
)

print("Cliente creado")

collection = client.get_or_create_collection(
    name="delivery_policies",
    embedding_function=None
)

print("Colección creada")

model = SentenceTransformer("all-MiniLM-L6-v2")

docs = [
    "El delivery tarda entre 30 y 45 minutos.",
    "Si el pedido llega frío, el cliente puede reclamar reembolso parcial.",
    "El repartidor debe confirmar la entrega en la app."
]

embeddings = model.encode(docs).tolist()

collection.add(
    ids=["policy_10", "policy_11", "policy_12"],
    documents=docs,
    embeddings=embeddings
)

print("OK embeddings guardados")