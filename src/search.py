import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.CloudClient(
    api_key="ck-6HbuPgtt1zi3ersMP5DuA3oY659ZdAKZiCSW79dWyELT",
    tenant="639f121d-09f8-4150-bfe5-7348282691e9",
    database="delivery_policy_rag"
)

collection = client.get_collection(
    name="delivery_policies_v2",
    embedding_function=None
)

model = SentenceTransformer("all-MiniLM-L6-v2")

question = "¿Puedo cancelar un pedido después de que fue asignado?"

query_embedding = model.encode([question]).tolist()[0]

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)

print("Pregunta:", question)
print("\nResultados:")

for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
    print("-", doc)
    print("  Fuente:", meta["source"])