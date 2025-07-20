from langchain.agents import Tool
from langchain_tools import (
    QueryDetectionsTool,
    AlertCheckTool,
    RetrieverTool,
    FrameRetrieverTool
)

def fuse_incident(query: str):
    print(f"\n🔍 Query: {query}")

    det_events = RetrieverTool.run(query)
    print("\n📦 Similar Detections:")
    for d in det_events:
        print(f"- {d}")

    frames = FrameRetrieverTool.run(query)
    print("\n🖼️ Matching Frames:")
    for f in frames:
        print(f"- {f}")

    alerts = AlertCheckTool.run("trigger")
    print("\n🚨 Alerts:")
    for a in alerts:
        print(f"- {a}")

    return det_events, frames, alerts

if __name__ == "__main__":
    fuse_incident("people near vehicles at night")
