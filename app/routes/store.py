from fastapi import APIRouter
from app.services.storage_service import save_result

router = APIRouter()

@router.post("/store")
def store(data: dict):
    return save_result(data)