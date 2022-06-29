from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import database
from .. import models

get_db = database.get_db

router = APIRouter(
    prefix="/menu",
    tags=['Meals']
)


@router.get("/{date}/{meal_type}")
def get_meals_by_date_and_type(date: str, meal_type: str, db: Session = Depends(get_db)):
    week = db.query(models.Week).filter(models.Week.start_date <=
                                        date, models.Week.end_date >= date).first()
    if not week:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Invalid date provided')
    meals = [meal.name for meal in week.meals if meal.type == meal_type]
    if not meals:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='No meals were found')
    return meals


@router.get("/{date}")
def get_meals_by_date(date: str, db: Session = Depends(get_db)):
    week = db.query(models.Week).filter(models.Week.start_date <=
                                        date, models.Week.end_date >= date).first()
    if not week:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Invalid date provided')
    if not week.meals:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='No meals were found')
    return week.meals
