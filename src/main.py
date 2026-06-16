from sentence_transformers import SentenceTransformer
from chroma_client import get_collection

model = SentenceTransformer("all-MiniLM-L6-v2")
collection = get_collection()

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