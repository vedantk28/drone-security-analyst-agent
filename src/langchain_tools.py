import sys, os, json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from langchain.agents import Tool
from src.detector_indexer import query_by_object
from src.alert_engine_v2 import check_alerts
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# 📁 Base paths
BASE_PATH = "/home/vedant/Desktop/drone_security_agent_project"
DETECTIONS_PATH = os.path.join(BASE_PATH, "data/detections.json")
VECTOR_INDEX = os.path.join(BASE_PATH, "data/vector_index")
FRAME_INDEX = os.path.join(BASE_PATH, "data/frame_index")

# 🧠 Detection-based object search
def query_detections(object_name: str):
    return query_by_object(object_name, filename=DETECTIONS_PATH)

QueryDetectionsTool = Tool.from_function(
    name="QueryDetectionsTool",
    func=query_detections,
    description="Search drone detections by object name (e.g., truck, crowd, person)"
)

# 🚨 Trigger alerts from detections
def run_alert_check(_: str):
    with open(DETECTIONS_PATH, "r") as f:
        detections = json.load(f)
    return check_alerts(detections)

AlertCheckTool = Tool.from_function(
    name="AlertCheckTool",
    func=run_alert_check,
    description="Check for triggered alerts based on detection rules"
)

# 🔍 Semantic search over detection logs
def semantic_search_detections(query: str):
    if not os.path.exists(VECTOR_INDEX):
        return ["[⚠️] Detection vector index missing."]
    embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    store = FAISS.load_local(
        VECTOR_INDEX,
        embeddings=embedder,
        allow_dangerous_deserialization=True
    )
    results = store.similarity_search(query, k=5)
    return [r.page_content for r in results]

RetrieverTool = Tool.from_function(
    name="SemanticRetrieverTool",
    func=semantic_search_detections,
    description="Find semantically similar detection events based on text query"
)

# 🖼️ Semantic search over frame captions
def semantic_search_frames(query: str):
    if not os.path.exists(FRAME_INDEX):
        return ["[⚠️] Frame index not found."]
    embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    store = FAISS.load_local(
        FRAME_INDEX,
        embeddings=embedder,
        allow_dangerous_deserialization=True
    )
    results = store.similarity_search(query, k=5)
    return [r.page_content for r in results]

FrameRetrieverTool = Tool.from_function(
    name="FrameRetrieverTool",
    func=semantic_search_frames,
    description="Retrieve semantically similar frame captions based on query"
)
