import sys, os
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
print("⚙️ Running input_generator tests...")

from src.input_generator import infer_location, generate_telemetry_from_captions

def test_location_mapping():
    assert infer_location("cars parked on street") == "Main Road"
    assert infer_location("gate visible behind fence") == "Main Gate"
    assert infer_location("trucks in the yard") == "Truck Yard"
    assert infer_location("an empty field") == "Unknown"

def test_generate_telemetry_structure():
    # Run the generator on test data
    generate_telemetry_from_captions("data/frame_captions.json")

    with open("data/telemetry.json") as f:
        data = json.load(f)

    # Check format of one sample entry
    assert isinstance(data, dict)
    assert len(data) > 0

    sample = next(iter(data.values()))
    assert "time" in sample and isinstance(sample["time"], str)
    assert "location" in sample and isinstance(sample["location"], str)
    assert "altitude" in sample and isinstance(sample["altitude"], float)
    assert 5.0 <= sample["altitude"] <= 20.0

if __name__ == "__main__":
    try:
        test_location_mapping()
        test_generate_telemetry_structure()
        print("✅ input_generator tests passed.")
    except AssertionError as e:
        print(f"❌ Test failed: {e}")
