import json
from src.frame_analyzer import FrameEvent

def save_indexed_events(events, filename="data/indexed_frames.json"):
    indexed = []
    for e in events:
        indexed.append({
            "timestamp": e.timestamp,
            "object": e.object,
            "location": e.location,
            "action": e.action
        })

    with open(filename, "w") as f:
        json.dump(indexed, f, indent=4)

def query_events_by_object(object_name, filename="data/indexed_frames.json"):
    with open(filename, "r") as f:
        data = json.load(f)

    return [e for e in data if object_name.lower() in e["object"].lower()]

if __name__ == "__main__":
    from src.input_generator import generate_sample_data
    from src.frame_analyzer import parse_description

    _, frames = generate_sample_data(6)
    events = [parse_description(f) for f in frames]

    save_indexed_events(events)

    print("\n--- Indexed Truck Events ---")
    truck_events = query_events_by_object("truck")
    for e in truck_events:
        print(e)
