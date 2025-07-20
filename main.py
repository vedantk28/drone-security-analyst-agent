import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from input_generator import generate_sample_data
from frame_analyzer import parse_description
from alert_engine import check_alerts
from indexer import save_indexed_events, query_events_by_object
from langchain_agent import execute_manual_workflow  # or import your DialoGPT agent function if customized

def run_pipeline(num_entries=6):
    print("\n Starting Drone Surveillance Pipeline...\n")

    # Step 1: Generate mock data
    telemetry_data, frame_data = generate_sample_data(num_entries)

    # Step 2: Parse frame descriptions
    events = [parse_description(f) for f in frame_data]
    print(f" Parsed {len(events)} frame events")

    # Step 3: Trigger alerts
    alerts = check_alerts(events)
    print("\n Alerts:")
    if alerts:
        for a in alerts:
            print(f" - {a}")
    else:
        print(" - No alerts triggered.")

    # Step 4: Save to FAISS index
    save_indexed_events(events)
    print("\n Saved indexed events to data/indexed_frames.json")

    # Step 5: Sample semantic query (truck)
    truck_events = query_events_by_object("truck")
    print("\n Queried Truck Events:")
    for e in truck_events:
        print(f" - {e['object']} at {e['location']} ({e['timestamp']})")

    # Step 6: Execute Agent Workflow (tool-powered reasoning)
    print("\nExecuting Investigation Agent...\n")
    execute_manual_workflow()

if __name__ == "__main__":
    run_pipeline()
