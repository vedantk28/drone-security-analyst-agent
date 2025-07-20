import json
import random
from datetime import datetime, timedelta

def infer_location(description: str) -> str:
    location_keywords = {
        "street": "Main Road",
        "city": "Urban Zone",
        "road": "Main Road",
        "parking": "Parking Lot",
        "lot": "Truck Yard",
        "yard": "Truck Yard",
        "dirt": "Side Access Road",
        "garage": "Garage",
        "gate": "Main Gate"
    }
    for keyword, location in location_keywords.items():
        if keyword in description.lower():
            return location
    return "Unknown"

def generate_telemetry_from_captions(captions_file="data/frame_captions.json"):
    with open(captions_file) as f:
        captions = json.load(f)

    base_time = datetime.strptime("00:00", "%H:%M")
    telemetry_data = {}

    for i, (img_name, description) in enumerate(captions.items()):
        timestamp = (base_time + timedelta(minutes=i)).strftime("%H:%M")
        location = infer_location(description)
        altitude = round(random.uniform(5.0, 20.0), 2)

        telemetry_data[img_name] = {
            "time": timestamp,
            "location": location,
            "altitude": altitude
        }

    with open("data/telemetry.json", "w") as f:
        json.dump(telemetry_data, f, indent=2)

    print("✅ Telemetry inferred and saved to data/telemetry.json")

if __name__ == "__main__":
    generate_telemetry_from_captions()
