import json
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# 🔍 Build FAISS from detection logs
def build_detection_index(filename="data/detections.json"):
    with open(filename, "r") as f:
        events = json.load(f)

    texts = []
    for e in events:
        txt = f"{e['object']} seen at {e['location']} around {e['timestamp']} (confidence: {e['confidence']})"
        texts.append(txt)

    embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    store = FAISS.from_texts(texts, embedding=embedder)
    store.save_local("data/vector_index")
    print("✅ Detection index built and saved to data/vector_index/")

# 🧠 Build FAISS from frame captions + telemetry
def build_frame_index(
    captions_file="data/frame_captions.json",
    telemetry_file="data/telemetry.json"
):
    with open(captions_file) as f:
        captions = json.load(f)
    with open(telemetry_file) as f:
        telemetry = json.load(f)

    texts = []
    for fname, caption in captions.items():
        meta = telemetry.get(fname, {})
        time = meta.get("time", "Unknown time")
        location = meta.get("location", "Unknown location")
        text = f"{fname}: {caption} [Location: {location}, Time: {time}]"
        texts.append(text)

    embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    store = FAISS.from_texts(texts, embedding=embedder)
    store.save_local("data/frame_index")
    print("✅ Frame index built and saved to data/frame_index/")

# 📦 Run both indexes
if __name__ == "__main__":
    build_detection_index()
    build_frame_index()
