import sys, os, json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from langchain.agents import Tool
from src.detector_indexer import query_by_object
from src.alert_engine_v2 import check_alerts
from src.frame_captioner import caption_all_images

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# ✅ Base paths for consistent retrieval
BASE_PATH = "/home/vedant/Desktop/drone_security_agent_project"
DETECTIONS_PATH = os.path.join(BASE_PATH, "data/detections.json")
VECTOR_INDEX = os.path.join(BASE_PATH, "data/vector_index")
FRAME_INDEX = os.path.join(BASE_PATH, "data/frame_index")

# 🧠 Detection-based object query
QueryDetectionsTool = Tool.from_function(
    name="QueryDetectionsTool",
    func=lambda q: query_by_object(q, filename=DETECTIONS_PATH),
    description="Query indexed drone detections by object name"
)

# 🚨 Alert logic execution
AlertCheckTool = Tool.from_function(
    name="AlertCheckTool",
    func=lambda _: check_alerts(json.load(open(DETECTIONS_PATH))),
    description="Run alert rules on drone detections and report any triggered alerts",
    args_schema=None
)

# 🔍 Semantic detection similarity search
def run_retriever(query):
    if not os.path.exists(VECTOR_INDEX):
        return ["[⚠️] Vector index not found."]
    embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    store = FAISS.load_local(
        VECTOR_INDEX,
        embeddings=embedder,
        allow_dangerous_deserialization=True  # ✅ Added for trusted pickle load
    )
    results = store.similarity_search(query, k=5)
    return [r.page_content for r in results]

RetrieverTool = Tool.from_function(
    name="SemanticRetrieverTool",
    func=run_retriever,
    description="Find detection events similar to a given query"
)

# 📸 Semantic frame caption retrieval
def query_frames(query):
    if not os.path.exists(FRAME_INDEX):
        return ["[⚠️] Frame index not found."]
    embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    store = FAISS.load_local(
        FRAME_INDEX,
        embeddings=embedder,
        allow_dangerous_deserialization=True  # ✅ Added for trusted pickle load
    )
    results = store.similarity_search(query, k=5)
    return [r.page_content for r in results]

FrameRetrieverTool = Tool.from_function(
    name="FrameRetrieverTool",
    func=query_frames,
    description="Retrieve visually described frames similar to a query"
)

# 🧪 Optional sanity check block
if __name__ == "__main__":
    print("\n🔍 QueryDetectionsTool:")
    for res in QueryDetectionsTool.run("car"):
        print(res)

    print("\n🚨 AlertCheckTool:")
    print(AlertCheckTool.run("trigger"))

    print("\n🧠 RetrieverTool:")
    for res in RetrieverTool.run("bus near the garage"):
        print(res)

    print("\n📸 FrameRetrieverTool:")
    for res in FrameRetrieverTool.run("people near buses at night"):
        print(res)
