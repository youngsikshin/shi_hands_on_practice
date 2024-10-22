from ultralytics import YOLO

model = YOLO("ship.pt")

results = model(['/home/yshin/datasets/ship/images/test/1-containershi_jpg.rf.590b26812ba203a67c2107649430e343.jpg']) 
#results = model(['/home/yshin/shi_hands_on_practice/yolov8/panama.mp4']) 

# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="datasets/train")  # save to disk
