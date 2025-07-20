from langchain_community.vectorstores import FAISS
from sentence_transformers import SentenceTransformer
from langchain_community.embeddings import HuggingFaceEmbeddings
from frame_captioner import caption_all_images


import json

def load_detection_texts(filename="data/detections.json"):
    with open(filename, "r") as f:
        events = json.load(f)

    texts = []
    for e in events:
        txt = f"{e['object']} seen at {e['location']} around {e['timestamp']} (confidence: {e['confidence']})"
        texts.append(txt)
    return texts

def build_faiss_store(filename="data/detections.json"):
    texts = load_detection_texts(filename)
    embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    store = FAISS.from_texts(texts, embedding=embedder)
    store.save_local("data/vector_index")






def build_frame_index():
    raw = caption_all_images(
        folder="/home/vedant/Desktop/drone_security_agent_project/data/visdrone/images",
        limit=5  # 🔍 Only captioned subset
    )
    texts = [f"{fname}: {caption}" for fname, caption in raw]

    embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    store = FAISS.from_texts(texts, embedding=embedder)
    store.save_local("data/frame_index")


if __name__ == "__main__":
    build_faiss_store()
    build_frame_index()

