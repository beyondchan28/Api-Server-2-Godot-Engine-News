from sqlalchemy.orm import Session
from sqlalchemy.sql.sqltypes import Integer
from fastapi import HTTPException,status
from .. import models, schemas


def get_all(db: Session):
    news = db.query(models.News).all()
    return news

def create(request: schemas.News, db: Session):
    new_news = models.News(title=request.title, thumbnail=request.thumbnail, source=request.source, content=request.content, author=request.author, year=request.year, user_id=1) #user_id msh hard coded
    db.add(new_news)
    db.commit()
    db.refresh(new_news)
    return new_news

def delete_one(id: Integer, db: Session):
    news = db.query(models.News).filter(models.News.id == id)
    if not news.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"news with id {id} is not exist.")
    news.delete(synchronize_session=False)
    db.commit()
    return "Data deleted successfully."

def update(id: Integer, request: schemas.News, db:Session):
    news = db.query(models.News).filter(models.News.id == id)
    if not news.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"news with id {id} is not exist.")
    news.update(request.dict())
    db.commit()
    return "Data updated successfully."

def get_one(id: Integer, db:Session):
    news = db.query(models.News).filter(models.News.id == id).first()
    if not news:
         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"news with id {id} is not exist.")
    return news