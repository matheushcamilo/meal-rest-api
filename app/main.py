from fastapi import FastAPI
from .routers import meal

app = FastAPI()

app.include_router(meal.router)