# app/models/news.py
from sqlalchemy import Column, Integer, String, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from app.database import Base


class NewsWebsite(Base):
    __tablename__ = "m02_news_websites"
    
    mnw_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    domain = Column(String(200), nullable=False)
    url = Column(String(300), nullable=False, unique=True)
    title = Column(String(1000), nullable=False)
    author = Column(String(150), nullable=False)
    date = Column(Date, nullable=True, index=True)
    date_txt = Column(String(50), nullable=True)
    content = Column(Text, nullable=False)