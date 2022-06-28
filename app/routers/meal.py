from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from .. import database
from .. import models
get_db = database.get_db

router = APIRouter(
    prefix="/menu", 
    tags=['Meals']
)

@router.get("/")
def get_meals_by_date_and_type(db: Session = Depends(get_db)):
    meal = db.query(models.Meal).filter(models.Meal.type == "MEAL_KIT").first()
    return meal