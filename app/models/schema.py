from pydantic import BaseModel
from typing import List

class ObjectDetection(BaseModel):
    label: str
    confidence: float
    bbox: List[float]

class PredictionResponse(BaseModel):
    objects: List[ObjectDetection]