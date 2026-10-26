from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}


@router.get("/add")
def add_numbers(a: int, b: int):
    return {"result": a + b}
