# app/main.py
from fastapi import FastAPI
from app.routers import news
from app.database import engine
from app.models import news as news_models


news_models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="AI Monitoring Topics API",
    description="API CRUD pour la base de données ai_monitoring_topics",
    version="0.1.0"
)


app.include_router(news.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to AI Monitoring Topics API"}

