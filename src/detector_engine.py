from dataclasses import dataclass

@dataclass
class DetectionEvent:
    timestamp: str
    location: str
    object: str
    confidence: float

def simulate_telemetry_for_images(img_files):
    locations = ["Gate", "Garage", "Main Road", "Backyard"]
    telemetry = []

    for i, file in enumerate(img_files):
        timestamp = f"00:{str(i+1).zfill(2)}"
        location = locations[i % len(locations)]
        telemetry.append((file, timestamp, location))

    return telemetry

from ultralytics import YOLO
import os

def detect_objects_with_telemetry(folder="data/visdrone/images", max_images=4, model_name="yolov8n.pt"):
    model = YOLO(model_name)
    img_files = sorted([f for f in os.listdir(folder) if f.endswith(".jpg")])[:max_images]
    telemetry = simulate_telemetry_for_images(img_files)

    events = []

    for file, timestamp, location in telemetry:
        path = os.path.join(folder, file)
        results = model(path)[0]

        for box in results.boxes:
            cls_id = int(box.cls[0])
            conf = round(float(box.conf[0]), 2)
            label = model.names[cls_id]

            events.append(DetectionEvent(
                timestamp=timestamp,
                location=location,
                object=label,
                confidence=conf
            ))

    return events

if __name__ == "__main__":
    detections = detect_objects_with_telemetry()
    print("\n🔍 Detection Events:")
    for d in detections:
        print(d)
