# rag.py
from openai import OpenAI
import chromadb

from utils import split_into_chunks

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("profile")

openai = OpenAI()

def index_profile(summary_text, pdf_text):
    docs = []
    for source in [("summary", summary_text), ("linkedin", pdf_text)]:
        chunks = split_into_chunks(source[1], chunk_size=800, overlap=120)
        for i, chunk in enumerate(chunks):
            docs.append({"id": f"{source[0]}-{i}", "text": chunk})
    for d in docs:
        emb = openai.embeddings.create(
            model="text-embedding-3-small",
            input=d["text"]
        ).data[0].embedding
        collection.add(ids=[d["id"]], embeddings=[emb], documents=[d["text"]])

def retrieve_context(question, k=4):
    q = openai.embeddings.create(
        model="text-embedding-3-small",
        input=question
    ).data[0].embedding
    results = collection.query(query_embeddings=[q], n_results=k)
    return "\n\n".join(results["documents"][0])