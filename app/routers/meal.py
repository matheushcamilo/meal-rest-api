from fastapi import APIRouter


router = APIRouter(
    prefix="/menu", 
    tags=['Meals']
)

@router.get("/")
def get_meals_by_date_and_type():
    return "Just a test to begin with"