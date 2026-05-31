'''
from ultralytics import YOLO
# Load pretrained YOLOv8 nano model
model = YOLO("yolov8n.pt")
# Train the model
results = model.train(
    data="data.yaml",
    epochs=30,
    imgsz=640,
    batch=8,
    project="models",
    name="ppe_detector"
)
print("Training completed!")

'''

from ultralytics import YOLO

# Load your saved checkpoint
model = YOLO("runs/detect/models/ppe_detector-2/weights/last.pt")

# Continue training   
results = model.train(
    data="data.yaml",
    epochs=10,
    imgsz=640,
    batch=8
)

print("Training completed!") 