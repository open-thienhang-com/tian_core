from fastapi import APIRouter

router = APIRouter()

@router.get("/liveness")
def liveness():
    return {"message": "success", "status": "ok"}