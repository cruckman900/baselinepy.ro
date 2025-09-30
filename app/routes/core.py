from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Welcome to fanTABulous!"}

@router.get("/health")
def health_check():
    return {"status": "fanTABulous is alive and riffing 🤘"}
