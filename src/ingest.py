from pathlib import Path

DOCUMENTS_DIR = Path("documents")

chunks = []

for file in DOCUMENTS_DIR.glob("*.txt"):
    text = file.read_text(encoding="utf-8")

    parts = [p.strip() for p in text.split("\n\n") if p.strip()]

    for i, part in enumerate(parts):
        chunks.append({
            "id": f"{file.stem}_{i}",
            "text": part,
            "source": file.name
        })

print("Chunks creados:", len(chunks))

for chunk in chunks:
    print("\nID:", chunk["id"])
    print("Source:", chunk["source"])
    print("Text:", chunk["text"])
    import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.CloudClient(
    api_key="ck-6HbuPgtt1zi3ersMP5DuA3oY659ZdAKZiCSW79dWyELT",
    tenant="639f121d-09f8-4150-bfe5-7348282691e9",
    database="delivery_policy_rag"
)

collection = client.get_or_create_collection(
    name="delivery_policies_v2",
    embedding_function=None
)

model = SentenceTransformer("all-MiniLM-L6-v2")

ids = [chunk["id"] for chunk in chunks]
documents = [chunk["text"] for chunk in chunks]
metadatas = [{"source": chunk["source"]} for chunk in chunks]
embeddings = model.encode(documents).tolist()

collection.add(
    ids=ids,
    documents=documents,
    metadatas=metadatas,
    embeddings=embeddings
)

print("OK guardado en Chroma Cloud")