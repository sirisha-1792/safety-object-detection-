from ultralytics import YOLO

# Load the trained model
model = YOLO("runs/detect/train/weights/best.pt")

# Predict on test images
results = model.predict(
    source="dataset/construction_site_safety/test/images",
    save=True,
    conf=0.25
)

print("Prediction completed!")