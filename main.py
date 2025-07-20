from src.input_generator import generate_sample_data
from src.frame_analyzer import parse_description
from src.alert_engine import check_alerts
from src.indexer import save_indexed_events, query_events_by_object

def run_agent(num_entries=6):
    print("🎮 Starting Drone Security Analyst Agent...\n")

    # Step 1: Generate mock telemetry and frame descriptions
    telemetry_data, frame_data = generate_sample_data(num_entries)

    # Step 2: Parse frame descriptions into structured events
    events = [parse_description(f) for f in frame_data]

    # Step 3: Check alerts
    alerts = check_alerts(events)
    print("🚨 Alerts Detected:")
    for a in alerts:
        print(f" - {a}")
    if not alerts:
        print(" - No alerts triggered.")

    # Step 4: Save events to index
    save_indexed_events(events)
    print("\n📦 Events indexed and saved to data/indexed_frames.json")

    # Step 5: Example query: all truck events
    truck_events = query_events_by_object("truck")
    print("\n🔍 Queried Truck Events:")
    for e in truck_events:
        print(f" - {e['object']} at {e['location']} ({e['timestamp']})")

if __name__ == "__main__":
    run_agent()
