from pathlib import Path
from sentence_transformers import SentenceTransformer
from chroma_client import get_collection

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

collection = get_collection()

model = SentenceTransformer("all-MiniLM-L6-v2")

ids = [chunk["id"] for chunk in chunks]
documents = [chunk["text"] for chunk in chunks]
metadatas = [{"source": chunk["source"]} for chunk in chunks]
embeddings = model.encode(documents).tolist()

collection.upsert(
    ids=ids,
    documents=documents,
    metadatas=metadatas,
    embeddings=embeddings
)

print("OK guardado en Chroma Cloud")