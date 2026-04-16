from fastapi import APIRouter, UploadFile, File
from app.services.yolo_service import run_inference
from app.utils.image_utils import read_image

router = APIRouter()

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = await read_image(file)
    result = run_inference(image)
    return result