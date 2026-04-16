from fastapi import APIRouter
from app.services.storage_service import load_results

router = APIRouter()

@router.get("/results")
def get_results():
    return {"data": load_results()}