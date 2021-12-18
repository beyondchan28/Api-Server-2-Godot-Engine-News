from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database, oauth2
from sqlalchemy.orm import Session
from ..repository import news

router = APIRouter(
    prefix="/news",
    tags=['News'],
    dependencies=[Depends(oauth2.get_current_user)]
)

get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowNews])
def news_show_all(db: Session = Depends(get_db)):
    return news.get_all(db)

@router.post('/', response_model=schemas.ShowNews, status_code=status.HTTP_201_CREATED)
def news_create(request: schemas.News, db: Session = Depends(get_db)):
    return news.create(request, db)

@router.get('/{id}', response_model=schemas.ShowNews, status_code=200)
def news_show(id: int,  db: Session = Depends(get_db)) :
     return news.get_one(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def news_update(id: int, request: schemas.News, db: Session = Depends(get_db) ):
    return news.update(id, request, db)
 
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def news_delete(id: int, db: Session = Depends(get_db)):
    return news.delete_one(id, db)