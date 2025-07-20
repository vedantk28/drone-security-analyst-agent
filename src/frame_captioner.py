# src/frame_captioner.py

# Treat the script as part of a Python package
__package__ = "src"

import os
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# 🧠 Caption a single image using BLIP
def caption_image(image_path):
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    image = Image.open(image_path).convert('RGB')
    inputs = processor(image, return_tensors="pt")
    output = model.generate(**inputs)
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption

# 📸 Caption multiple images (limit helps for testing!)
def caption_all_images(folder="/home/vedant/Desktop/drone_security_agent_project/data/visdrone/images", limit=10):
    all_images = sorted(
        [f for f in os.listdir(folder) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    )[:limit]

    captions = []
    for fname in all_images:
        path = os.path.join(folder, fname)
        try:
            text = caption_image(path)
            captions.append((fname, text))
            print(f"[✅] {fname}: {text}")
        except Exception as e:
            print(f"[⚠️] Skipping {fname}: {e}")
    return captions

# 🔧 Manual test block
if __name__ == "__main__":
    results = caption_all_images(
        folder="/home/vedant/Desktop/drone_security_agent_project/data/visdrone/images",
        limit=10
    )
    print("\n📋 Summary:")
    for fname, caption in results:
        print(f"{fname}: {caption}")

    # 💾 Save to file
    import json
    captions_dict = {fname: caption for fname, caption in results}
    with open("data/frame_captions.json", "w") as f:
        json.dump(captions_dict, f, indent=2)
    print("✅ Captions saved to data/frame_captions.json")

