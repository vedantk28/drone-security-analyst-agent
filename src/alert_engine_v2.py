from datetime import datetime

def check_alerts(events):
    alerts = []

    for e in events:
        time_obj = datetime.strptime(e["timestamp"], "%H:%M")
        hour = time_obj.hour

        # Rule 1: Person at Gate after midnight (00:00–01:00)
        if e["object"].lower() == "person" and "gate" in e["location"].lower():
            if hour == 0:
                msg = f"ALERT: {e['object']} near {e['location']} at {e['timestamp']}"
                alerts.append(msg)

        # Rule 2: Bus detected with low confidence (possible anomaly)
        if e["object"].lower() == "bus" and e["confidence"] < 0.35:
            msg = f"ALERT: Low-confidence bus detection at {e['location']} [{e['confidence']}]"
            alerts.append(msg)

        # Rule 3: Repeated Car Detection at Main Road (we’ll refine this later)
        # Placeholder for tracking over time

    return alerts

if __name__ == "__main__":
    import json
    with open("data/detections.json", "r") as f:
        events = json.load(f)

    alerts = check_alerts(events)

    print("\n Triggered Alerts:")
    for alert in alerts:
        print(" -", alert)

    if not alerts:
        print(" - No alerts triggered.")
