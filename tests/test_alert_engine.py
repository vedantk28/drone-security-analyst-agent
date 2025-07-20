import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
print("⚙️ Running alert_engine tests...")

from src.alert_engine import check_alerts
from src.frame_analyzer import FrameEvent

def test_midnight_alert():
    event = FrameEvent(timestamp="00:03", object="Person", location="Gate", action="spotted")
    alerts = check_alerts([event])
    assert len(alerts) == 1
    assert "loitering at Gate" in alerts[0]

def test_non_alert():
    event = FrameEvent(timestamp="14:15", object="Dog", location="Garage", action="spotted")
    alerts = check_alerts([event])
    assert alerts == []

if __name__ == "__main__":
    test_midnight_alert()
    test_non_alert()
    print("✅ alert_engine tests passed.")
