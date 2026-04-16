from ultralytics import YOLO
from app.config import MODEL_PATH, CONF_THRESHOLD

# Load model once (important)
model = YOLO(MODEL_PATH)

def run_inference(image):
    results = model(image)

    detections = []

    for r in results:
        for box in r.boxes:
            conf = float(box.conf)

            if conf < CONF_THRESHOLD:
                continue

            detections.append({
                "label": model.names[int(box.cls)],
                "confidence": conf,
                "bbox": box.xyxy.tolist()[0]
            })

    return {"objects": detections}