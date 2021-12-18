from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class News(Base):
    __tablename__ = 'news'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    thumbnail = Column(String)
    source = Column(String)
    content = Column(String)
    author = Column(String)
    year = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    creator = relationship("User", back_populates="news")

class User(Base):
    __tablename__='users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    
    news = relationship('News', back_populates="creator")
    