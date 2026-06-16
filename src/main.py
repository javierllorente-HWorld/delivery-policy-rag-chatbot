from langchain_community.document_loaders import TextLoader

documents = []

for file_name in [
    "documents/refund_policy.txt",
    "documents/cancellation_policy.txt",
    "documents/driver_rules.txt",
]:
    loader = TextLoader(file_name, encoding="utf-8")
    documents.extend(loader.load())

print("Documentos cargados:", len(documents))

for doc in documents:
    print("\n------------------")
    print(doc.page_content)