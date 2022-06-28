from .database import Base
from sqlalchemy import Column, String, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship

meal_week = Table('meal_week', Base.metadata,
    Column('meal_id', ForeignKey('meal.id'), primary_key=True),
    Column('week_id', ForeignKey('week.id'), primary_key=True)
)

class Meal(Base):
    __tablename__ = 'meal'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String)

    weeks = relationship("Week", secondary="meal_week", back_populates="meals")

class Week(Base):
    __tablename__ = 'week'

    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(String, nullable=False)
    end_date = Column(String, nullable=False)    

    meals = relationship("Meal", secondary="meal_week", back_populates="weeks")