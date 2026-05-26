from sqlalchemy import true
from ultralytics import YOLO

model = YOLO("yolo11n-seg.pt")

model.train(
    data="data.yaml",          
    epochs=120,                
    imgsz=640,                 
    batch=8,
    device="cpu",              
    project="runs_puzzle",
    name="yolo11n-seg-maca-reparametros-121125",

    lr0=0.001,
    lrf=0.01,
    optimizer="AdamW",
    momentum=0.9,
    weight_decay=0.0005,
    warmup_epochs=3.0,
    warmup_momentum=0.5,
    warmup_bias_lr=0.05,

    hsv_h=0.015,
    hsv_s=0.7,
    hsv_v=0.4,          

    degrees=90.0,       
    translate=0.20,     
    scale=0.6,         
    shear=10.0,         
    perspective=0.001,  

    flipud=0.0,         
    fliplr=0.0,         

    mosaic=0.7,         
    mixup=0.0,
    copy_paste=0.8,     
    auto_augment="randaugment",
    erasing=0.5,       

    patience=25,
    save=True,
    plots=True,
)