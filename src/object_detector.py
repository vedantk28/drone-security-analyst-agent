from ultralytics import YOLO
import os

def run_detection_on_folder(folder="data/visdrone/images", max_images=3, model_name="yolov8n.pt"):
    model = YOLO(model_name)
    img_files = sorted([f for f in os.listdir(folder) if f.endswith(".jpg")])[:max_images]

    for file in img_files:
        path = os.path.join(folder, file)
        results = model(path)[0]

        print(f"\n📸 {file} — {len(results.boxes)} detections")
        for box in results.boxes:
            cls_id = int(box.cls[0])
            conf = round(float(box.conf[0]), 2)
            label = model.names[cls_id]
            print(f" - {label} ({conf})")

if __name__ == "__main__":
    run_detection_on_folder()
