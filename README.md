# shi_hands_on_practice

## Cloning the repository

```
git clone https://github.com/youngsikshin/shi_hands_on_practice.git
```

## YOLOv8

### 1. Conda Install

https://docs.anaconda.com/miniconda/miniconda-other-installer-links/

### 2. Conda environment

```
$ conda create -n yolov8 python==3.10
$ conda activate yolov8
```

### 3. yolo install

```
pip install ultralytics
pip install opencv-python
```

examples
```
from ultralytics import YOLO

# Create a new YOLO model from scratch
model = YOLO("yolov8n.yaml")

# Load a pretrained YOLO model (recommended for training)
model = YOLO("yolov8n.pt")

# Train the model using the 'coco8.yaml' dataset for 3 epochs
results = model.train(data="coco8.yaml", epochs=3)

# Evaluate the model's performance on the validation set
results = model.val()

# Perform object detection on an image using the model
results = model("https://ultralytics.com/images/bus.jpg")
```

Dataset download
```
$ cd yolov8
$ mkdir datasets
$ cd datasets
$ pip install gdown
$ gdown https://drive.google.com/uc?id=1rvv8kgaAK-aOT-F-EhgcuorxADnDHpSB
$ unzip ship.zip
```

### roboflow dataset link

https://universe.roboflow.com/liu-yang-yhkts/myships-qs6dm/dataset/10
