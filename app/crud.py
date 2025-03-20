from sqlalchemy.orm import Session
from .models import Topic

class CRUD:
    def create_topic(self, db: Session, title: str, description: str):
        db_topic = Topic(title=title, description=description)
        db.add(db_topic)
        db.commit()
        db.refresh(db_topic)
        return db_topic

    def get_topic(self, db: Session, topic_id: int):
        return db.query(Topic).filter(Topic.id == topic_id).first()

    def get_topics(self, db: Session, skip: int = 0, limit: int = 10):
        return db.query(Topic).offset(skip).limit(limit).all()

    def update_topic(self, db: Session, topic_id: int, title: str, description: str):
        db_topic = db.query(Topic).filter(Topic.id == topic_id).first()
        if db_topic:
            db_topic.title = title
            db_topic.description = description
            db.commit()
            db.refresh(db_topic)
        return db_topic

    def delete_topic(self, db: Session, topic_id: int):
        db_topic = db.query(Topic).filter(Topic.id == topic_id).first()
        if db_topic:
            db.delete(db_topic)
            db.commit()
        return db_topic
