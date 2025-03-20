from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import Database
from .crud import CRUD

app = FastAPI()

# database = Database()
# crud = CRUD()

@app.get("/")
def read_root():
    return 'coco'

# @app.post("/topics/")
# def create_topic(title: str, description: str, db: Session = Depends(database.get_db)):
#     return crud.create_topic(db=db, title=title, description=description)

# @app.get("/topics/{topic_id}")
# def get_topic(topic_id: int, db: Session = Depends(database.get_db)):
#     return crud.get_topic(db=db, topic_id=topic_id)

# @app.get("/topics/")
# def get_topics(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
#     return crud.get_topics(db=db, skip=skip, limit=limit)

# @app.put("/topics/{topic_id}")
# def update_topic(topic_id: int, title: str, description: str, db: Session = Depends(database.get_db)):
#     return crud.update_topic(db=db, topic_id=topic_id, title=title, description=description)

# @app.delete("/topics/{topic_id}")
# def delete_topic(topic_id: int, db: Session = Depends(database.get_db)):
#     return crud.delete_topic(db=db, topic_id=topic_id)
