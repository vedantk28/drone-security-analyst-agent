from src.frame_analyzer import FrameEvent
from datetime import datetime

def check_alerts(events):
    alerts = []
    for event in events:
        # Convert timestamp string to datetime object
        time_obj = datetime.strptime(event.timestamp, "%H:%M")
        hour = time_obj.hour

        # Rule 1: Person loitering after midnight near Gate
        if event.object.lower().startswith("person"):
            if hour == 0 and "gate" in event.location.lower():
                alert_msg = f"ALERT: {event.object} loitering at {event.location}, {event.timestamp}"
                alerts.append(alert_msg)

        # Rule 2 placeholder (to be expanded later)
        # e.g., count similar vehicle detections

    return alerts

if __name__ == "__main__":
    from frame_analyzer import FrameEvent
    test_events = [
        FrameEvent(timestamp="00:05", object="Person", location="Gate", action="spotted"),
        FrameEvent(timestamp="14:22", object="Dog", location="Backyard", action="spotted"),
        FrameEvent(timestamp="00:15", object="Person", location="Garage", action="spotted"),
    ]

    print("\n--- Alerts ---")
    alerts = check_alerts(test_events)
    for alert in alerts:
        print(alert)

