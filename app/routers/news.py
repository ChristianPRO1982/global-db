# app/routers/news.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.models.news import NewsWebsite
from app.schemas.news import NewsWebsiteCreate, NewsWebsite as NewsWebsiteSchema, NewsWebsiteUpdate


router = APIRouter(
    prefix="/news",
    tags=["news"]
)


@router.post("/", response_model=NewsWebsiteSchema, status_code=status.HTTP_201_CREATED)
def create_news_website(news: NewsWebsiteCreate, db: Session = Depends(get_db)):
    db_news = NewsWebsite(**news.dict())
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news


@router.get("/", response_model=List[NewsWebsiteSchema])
def read_news_websites(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    news = db.query(NewsWebsite).offset(skip).limit(limit).all()
    return news


@router.get("/{news_id}", response_model=NewsWebsiteSchema)
def read_news_website(news_id: int, db: Session = Depends(get_db)):
    db_news = db.query(NewsWebsite).filter(NewsWebsite.mnw_id == news_id).first()
    if db_news is None:
        raise HTTPException(status_code=404, detail="News website not found")
    return db_news


@router.put("/{news_id}", response_model=NewsWebsiteSchema)
def update_news_website(news_id: int, news: NewsWebsiteUpdate, db: Session = Depends(get_db)):
    db_news = db.query(NewsWebsite).filter(NewsWebsite.mnw_id == news_id).first()
    if db_news is None:
        raise HTTPException(status_code=404, detail="News website not found")
    
    update_data = news.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_news, key, value)
    
    db.commit()
    db.refresh(db_news)
    return db_news


@router.delete("/{news_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_news_website(news_id: int, db: Session = Depends(get_db)):
    db_news = db.query(NewsWebsite).filter(NewsWebsite.mnw_id == news_id).first()
    if db_news is None:
        raise HTTPException(status_code=404, detail="News website not found")
    
    db.delete(db_news)
    db.commit()
    return None