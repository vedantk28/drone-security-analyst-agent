import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



import json
from src.detector_engine import DetectionEvent

def save_detections_to_json(events, filename="data/detections.json"):
    data = []
    for e in events:
        data.append({
            "timestamp": e.timestamp,
            "location": e.location,
            "object": e.object,
            "confidence": e.confidence
        })

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def query_by_object(object_name, filename="data/detections.json"):
    with open(filename, "r") as f:
        detections = json.load(f)

    return [d for d in detections if object_name.lower() in d["object"].lower()]

if __name__ == "__main__":
    from src.detector_engine import detect_objects_with_telemetry

    events = detect_objects_with_telemetry()
    save_detections_to_json(events)

    print("\n🔍 Queried Car Detections:")
    car_hits = query_by_object("car")
    for hit in car_hits:
        print(f"{hit['object']} at {hit['location']} ({hit['timestamp']}) [{hit['confidence']}]")
