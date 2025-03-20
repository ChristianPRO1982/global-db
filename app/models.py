from sqlalchemy import Column, Integer, String
from .database import Database

class Topic(Database.Base):
    __tablename__ = 'topics'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    description = Column(String(2000))
