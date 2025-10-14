from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Welcome to NEXTRiff"}

@router.get("/health")
def health_check():
    return {"status": "ok"}
