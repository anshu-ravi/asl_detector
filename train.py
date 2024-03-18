from ultralytics import YOLO


IMG_SIZE = 640
BATCH_SIZE = 8
EPOCHS = 50
DATA_PATH = 'data/data.yaml'
EXP_NAME = 'yolov8n_asl'
MODEL = 'yolov8n.pt'

# Train the model
model = YOLO(MODEL)
results = model.train(
   data=DATA_PATH,
   imgsz=IMG_SIZE,
   epochs=EPOCHS,
   batch=BATCH_SIZE,
   name=EXP_NAME
)
