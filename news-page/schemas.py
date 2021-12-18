from typing import List, Optional
from pydantic import BaseModel

class NewsBase(BaseModel):
    title: str
    thumbnail: str
    source: str
    content: str
    author: str
    year: int

class News (NewsBase):
    class Config():
        orm_mode= True

class User(BaseModel):
    name: str
    email: str
    password: str
    

class ShowUser(BaseModel):
    name: str
    email: str
    news: List[News]
    class Config():
        orm_mode= True
        

class UserForNews(BaseModel):
    name: str
    email: str
    class Config():
        orm_mode= True

class ShowNews(BaseModel):
    title: str
    thumbnail: str
    source: str
    content: str
    author: str
    year: int
    creator: UserForNews
    class Config():
        orm_mode= True

class Login(BaseModel):
    username: str
    password: str

class TokenData(BaseModel):
    email: Optional[str] = None