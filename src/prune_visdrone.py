import os
import shutil

# Original folders
IMAGES_DIR = "data/visdrone/images"
ANNOT_DIR = "data/visdrone/annotations"

# Temp sample folder
SAMPLED_IMAGES_DIR = "data/visdrone_sample/images"
SAMPLED_ANNOT_DIR = "data/visdrone_sample/annotations"

# Create sample folders
os.makedirs(SAMPLED_IMAGES_DIR, exist_ok=True)
os.makedirs(SAMPLED_ANNOT_DIR, exist_ok=True)

# Grab first 10 images
all_images = sorted([f for f in os.listdir(IMAGES_DIR) if f.endswith(".jpg")])
sample_images = all_images[:10]

for img_name in sample_images:
    base_name = os.path.splitext(img_name)[0]
    annot_name = base_name + ".txt"

    # Copy image
    shutil.copy(os.path.join(IMAGES_DIR, img_name), os.path.join(SAMPLED_IMAGES_DIR, img_name))

    # Copy matching annotation if exists
    annot_path = os.path.join(ANNOT_DIR, annot_name)
    if os.path.exists(annot_path):
        shutil.copy(annot_path, os.path.join(SAMPLED_ANNOT_DIR, annot_name))
    else:
        print(f"[⚠️] Annotation missing for {img_name}")

print("✅ Sample created with 10 images and annotations.")

# 💡 Optional: replace original VisDrone folders
confirm = input("Replace original VisDrone data with sample? (y/n): ")
if confirm.lower() == "y":
    shutil.rmtree(IMAGES_DIR)
    shutil.rmtree(ANNOT_DIR)
    shutil.move(SAMPLED_IMAGES_DIR, IMAGES_DIR)
    shutil.move(SAMPLED_ANNOT_DIR, ANNOT_DIR)
    print("✅ VisDrone dataset shrunk to sample set.")
else:
    print("ℹ️ Original data retained. Sample stored in 'data/visdrone_sample'")
