import faiss
import numpy as np
from services.gpt_client import get_chat_client, get_embedding_model_name

DIMENSION = 1536  # OpenAI text-embedding-3-small size
index = faiss.IndexFlatL2(DIMENSION)
documents = []

def create_embedding(text: str):
    client = get_chat_client()
    response = client.embeddings.create(
        model=get_embedding_model_name(),
        input=text
    )
    return np.array(response.data[0].embedding).astype("float32")

def add_documents(chunks: list[str]):
    for chunk in chunks:
        emb = create_embedding(chunk)
        index.add(np.array([emb]))
        documents.append(chunk)

def search(query: str, k=4):
    client = get_chat_client()
    response = client.embeddings.create(
        model=get_embedding_model_name(),
        input=query
    )
    q_emb = np.array(response.data[0].embedding).astype("float32")
    
    distances, indices = index.search(np.array([q_emb]), k)

    return [documents[i] for i in indices[0] if i < len(documents)]
