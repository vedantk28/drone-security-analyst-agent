from dataclasses import dataclass
import random
from datetime import datetime, timedelta

@dataclass
class TelemetryEntry:
    timestamp: str
    location: str
    altitude: float

@dataclass
class FrameDescription:
    timestamp: str
    description: str

def generate_sample_data(num_entries=5):
    locations = ["Gate", "Garage", "Main Road", "Backyard"]
    objects = ["Blue truck", "Person", "Dog", "Black SUV"]

    base_time = datetime.now()
    telemetry = []
    frames = []

    for i in range(num_entries):
        time = base_time + timedelta(minutes=i)
        time_str = time.strftime("%H:%M")

        # Telemetry simulation
        loc = random.choice(locations)
        alt = round(random.uniform(5.0, 20.0), 2)
        telemetry.append(TelemetryEntry(timestamp=time_str, location=loc, altitude=alt))

        # Frame description simulation
        obj = random.choice(objects)
        frames.append(FrameDescription(timestamp=time_str, description=f"{obj} spotted at {loc}"))

    return telemetry, frames

if __name__ == "__main__":
    telemetry_data, frame_data = generate_sample_data()

    print("\n--- Telemetry ---")
    for entry in telemetry_data:
        print(entry)

    print("\n--- Frame Descriptions ---")
    for frame in frame_data:
        print(frame)
