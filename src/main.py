from sentence_transformers import SentenceTransformer

documents = [
    "Los clientes pueden solicitar un reembolso dentro de las 48 horas posteriores a la entrega.",
    "Los pedidos pueden cancelarse antes de ser asignados a un repartidor.",
    "Los repartidores deben completar las entregas a tiempo."
]

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(documents)

print("Cantidad de embeddings:", len(embeddings))
print("Dimensión del vector:", len(embeddings[0]))

print("\nPrimer embedding:")
print(embeddings[0])