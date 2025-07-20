import json
from datetime import datetime
from src.frame_analyzer import FrameEvent

def check_alerts(events):
    alerts = []

    for event in events:
        time_obj = datetime.strptime(event.timestamp, "%H:%M")
        hour = time_obj.hour

        # Rule 1: Person loitering after midnight near Gate
        if event.object.lower().startswith("person"):
            if hour == 0 and "gate" in event.location.lower():
                alerts.append(f"ALERT: {event.object} loitering at {event.location}, {event.timestamp}")

        # Rule 2: Crowd detected in Urban Zone
        if "crowd" in event.object.lower() and "urban" in event.location.lower():
            alerts.append(f"ALERT: Crowd detected in {event.location} at {event.timestamp}")

        # Rule 3: Trucks clustered in Truck Yard
        if "truck" in event.object.lower() and "yard" in event.location.lower():
            alerts.append(f"ALERT: Truck cluster detected at {event.location}, {event.timestamp}")

    return alerts

def load_events(captions_file="data/frame_captions.json", telemetry_file="data/telemetry.json"):
    with open(captions_file) as f:
        captions = json.load(f)
    with open(telemetry_file) as f:
        telemetry = json.load(f)

    events = []
    for fname, caption in captions.items():
        meta = telemetry.get(fname, {})
        timestamp = meta.get("time", "00:00")
        location = meta.get("location", "Unknown")
        events.append(FrameEvent(timestamp=timestamp, object=caption, location=location, action="captioned"))

    return events

if __name__ == "__main__":
    events = load_events()
    alerts = check_alerts(events)

    print("\n--- Alerts ---")
    for alert in alerts:
        print(alert)

    with open("data/alerts.json", "w") as f:
        json.dump(alerts, f, indent=2)

    print("✅ Alerts saved to data/alerts.json")
