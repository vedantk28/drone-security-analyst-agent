import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.langchain_tools import (
    QueryDetectionsTool,
    AlertCheckTool,
    RetrieverTool,
    FrameRetrieverTool
)

# 🚀 Manual investigation workflow (No agent)
def execute_manual_workflow():
    query = "Investigate any suspicious events involving buses or crowds near the Garage"
    print(f"\n🔍 Investigation Query: {query}")
    print("=" * 60)

    results = {}

    # Step 1: Alerts
    print("\n📋 Step 1: Checking alerts...")
    try:
        results['alerts'] = AlertCheckTool.invoke("")
    except Exception as e:
        results['alerts'] = f"❌ Alert check failed: {e}"

    # Step 2: Bus detections
    print("\n🚌 Step 2: Bus detections...")
    try:
        results['bus_detections'] = QueryDetectionsTool.invoke("bus")
    except Exception as e:
        results['bus_detections'] = f"❌ Bus detection failed: {e}"

    # Step 3: Crowd detections
    print("\n👥 Step 3: Crowd detections...")
    try:
        results['crowd_detections'] = QueryDetectionsTool.invoke("crowd")
    except Exception as e:
        results['crowd_detections'] = f"❌ Crowd detection failed: {e}"

    # Step 4: Semantic search near garage
    print("\n🏢 Step 4: Semantic search near garage...")
    try:
        results['garage_events'] = RetrieverTool.invoke("suspicious activity near garage")
    except Exception as e:
        results['garage_events'] = f"❌ Garage search failed: {e}"

    # Step 5: Visual frame retrieval
    print("\n🖼️ Step 5: Visual frames...")
    try:
        results['visual_frames'] = FrameRetrieverTool.invoke("bus crowd garage")
    except Exception as e:
        results['visual_frames'] = f"❌ Frame retrieval failed: {e}"

    # Final Summary
    print("\n🧠 INVESTIGATION SUMMARY")
    print("=" * 60)
    for key, value in results.items():
        print(f"\n{key.upper()}: {value}")

    return results

# 🏁 Entry point
if __name__ == "__main__":
    print("\n🎯 RUNNING MANUAL INVESTIGATION WORKFLOW")
    execute_manual_workflow()
