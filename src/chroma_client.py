import chromadb

API_KEY = "ck-6HbuPgtt1zi3ersMP5DuA3oY659ZdAKZiCSW79dWyELT"
TENANT = "639f121d-09f8-4150-bfe5-7348282691e9"
DATABASE = "delivery_policy_rag"
COLLECTION_NAME = "delivery_policies_v2"


def get_collection():
    client = chromadb.CloudClient(
        api_key=API_KEY,
        tenant=TENANT,
        database=DATABASE
    )

    collection = client.get_collection(
        name=COLLECTION_NAME,
        embedding_function=None
    )

    return collection