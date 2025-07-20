import os
from PIL import Image

def load_visdrone_images(folder="/home/vedant/Desktop/drone_security_agent_project/data/visdrone/images", max_images=5):
    img_files = [f for f in os.listdir(folder) if f.endswith(".jpg")]
    img_files.sort()

    samples = img_files[:max_images]
    for file in samples:
        path = os.path.join(folder, file)
        img = Image.open(path)
        print(f"Loaded: {file} - Size: {img.size}")
        img.show()  # opens in system viewer (can be skipped if headless)

if __name__ == "__main__":
    load_visdrone_images()
