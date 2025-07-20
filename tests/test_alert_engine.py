import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

print("⚙️ Running alert_engine tests...")

from src.alert_engine import check_alerts
from src.frame_analyzer import FrameEvent

def test_person_loitering_midnight():
    event = FrameEvent(timestamp="00:03", object="Person", location="Gate", action="captioned")
    alerts = check_alerts([event])
    assert isinstance(alerts, list)
    assert len(alerts) == 1
    assert "loitering at Gate" in alerts[0]

def test_crowd_in_urban_zone():
    event = FrameEvent(timestamp="09:42", object="large crowd", location="Urban Zone", action="captioned")
    alerts = check_alerts([event])
    assert len(alerts) == 1
    assert "Crowd detected in Urban Zone" in alerts[0]

def test_truck_cluster():
    event = FrameEvent(timestamp="11:15", object="truck", location="Truck Yard", action="captioned")
    alerts = check_alerts([event])
    assert len(alerts) == 1
    assert "Truck cluster detected at Truck Yard" in alerts[0]

def test_non_alert_case():
    event = FrameEvent(timestamp="15:27", object="dog", location="Garage", action="captioned")
    alerts = check_alerts([event])
    assert alerts == []

if __name__ == "__main__":
    try:
        test_person_loitering_midnight()
        test_crowd_in_urban_zone()
        test_truck_cluster()
        test_non_alert_case()
        print("✅ alert_engine tests passed.")
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
