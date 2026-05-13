from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Hero(Base):
    __tablename__ = "heroes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    difficulty = Column(String)
    description = Column(Text)

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    hero_name = Column(String)
    user_name = Column(String)
    content = Column(Text)
    rating = Column(Integer)