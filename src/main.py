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

print("Chatbot de políticas de delivery")
print("Escribí 'salir' para terminar")

while True:
    question = input("\nPregunta: ")

    if question.lower() == "salir":
        break

    query_embedding = model.encode([question]).tolist()[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=2
    )

    docs = results["documents"][0]
    metas = results["metadatas"][0]

    sources = sorted(set(meta["source"] for meta in metas))
    answer = " ".join(docs)

    print("\nRespuesta:")
    print(answer)

    print("\nFuentes:")
    for source in sources:
        print("-", source)