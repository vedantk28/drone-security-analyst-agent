import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.detector_engine import DetectionEvent
from src.detector_indexer import save_detections_to_json, query_by_object
from src.alert_engine_v2 import check_alerts
import json

def test_indexing_and_query():
    # Prepare mock events
    mock_events = [
        DetectionEvent(timestamp="00:01", location="Gate", object="person", confidence=0.92),
        DetectionEvent(timestamp="00:04", location="Garage", object="car", confidence=0.88),
        DetectionEvent(timestamp="00:05", location="Main Road", object="bus", confidence=0.29)
    ]

    # Save to test file
    save_detections_to_json(mock_events, filename="data/test_detections.json")

    # Test query
    cars = query_by_object("car", filename="data/test_detections.json")
    assert len(cars) == 1
    assert cars[0]["location"] == "Garage"

def test_alert_logic():
    # Load mock data
    with open("data/test_detections.json", "r") as f:
        test_events = json.load(f)

    alerts = check_alerts(test_events)

    assert any("person" in a.lower() for a in alerts)
    assert any("bus" in a.lower() and "low-confidence" in a.lower() for a in alerts)

if __name__ == "__main__":
    test_indexing_and_query()
    test_alert_logic()
    print("✅ Real-world pipeline tests passed.")
