from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")

image_path = input("Enter image path: ")

results = model.predict(
    source=image_path,
    save=True
)

print("Prediction completed!")