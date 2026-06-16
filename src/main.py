from sentence_transformers import SentenceTransformer
from chroma_client import get_collection

POLICY_KEYWORDS = [
    "pedido",
    "delivery",
    "entrega",
    "reembolso",
    "devolución",
    "devolver",
    "plata",
    "dinero",
    "cancelar",
    "cancelación",
    "repartidor",
    "demora",
    "retraso",
    "tarde",
    "soporte",
    "cuenta",
    "suspensión",
]

model = SentenceTransformer("all-MiniLM-L6-v2")
collection = get_collection()

print("Chatbot de políticas de delivery")
print("Escribí 'salir' para terminar")


def is_policy_question(question):
    question_lower = question.lower()
    return any(keyword in question_lower for keyword in POLICY_KEYWORDS)


while True:
    question = input("\nPregunta: ")

    if question.lower() == "salir":
        break

    if not is_policy_question(question):
        print("\nRespuesta:")
        print("No encontré información suficiente en las políticas cargadas.")
        continue

    query_embedding = model.encode([question]).tolist()[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=2
    )

    docs = results["documents"][0]
    metas = results["metadatas"][0]

    if not docs:
        print("\nRespuesta:")
        print("No encontré información suficiente en las políticas cargadas.")
        continue

    sources = sorted(set(meta["source"] for meta in metas))
    answer = " ".join(docs)

    print("\nRespuesta:")
    print(answer)

    print("\nFuentes:")
    for source in sources:
        print("-", source)