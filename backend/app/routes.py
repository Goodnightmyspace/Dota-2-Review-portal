from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Hero, Review

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/heroes")
def get_heroes(db: Session = Depends(get_db)):
    return db.query(Hero).all()

@router.get("/reviews")
def get_reviews(db: Session = Depends(get_db)):
    return db.query(Review).all()

@router.post("/reviews")
def create_review(review_data: dict, db: Session = Depends(get_db)):
    new_review = Review(
        hero_name=review_data['hero_name'],
        user_name=review_data['user_name'],
        text=review_data['text'],
        rating=review_data['rating']
    )
    db.add(new_review)
    db.commit()
    return {"status": "success"}