# app/schemas/news.py
from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import date


class NewsWebsiteBase(BaseModel):
    domain: str
    url: str
    title: str
    author: str
    date: Optional[date] = None
    date_txt: Optional[str] = None
    content: str


class NewsWebsiteCreate(NewsWebsiteBase):
    pass


class NewsWebsiteUpdate(BaseModel):
    domain: Optional[str] = None
    url: Optional[str] = None
    title: Optional[str] = None
    author: Optional[str] = None
    date: Optional[date] = None
    date_txt: Optional[str] = None
    content: Optional[str] = None


class NewsWebsiteInDB(NewsWebsiteBase):
    mnw_id: int
    
    class Config:
        orm_mode = True
        

class NewsWebsite(NewsWebsiteInDB):
    pass