from ultralytics import YOLO

model = YOLO("yolov8n.yaml")
model = YOLO("yolov8n.pt")
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
results = model.train(data="ship.yaml", epochs=100, imgsz=640)
