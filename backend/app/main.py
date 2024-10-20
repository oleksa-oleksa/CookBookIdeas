from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, database, schemas
from app.schemas import ReceiptCreate  # Explicitly import ReceiptCreate
from app.models import Receipt
from app.database import get_db
from datetime import datetime

app = FastAPI()

# Create the database tables
models.Base.metadata.create_all(bind=database.engine)

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/receipts/")
def create_receipt(receipt: ReceiptCreate, db: Session = Depends(get_db)):
    # Create an instance of the SQLAlchemy model
    db_receipt = models.Receipt(
        title=receipt.title,
        photo_url=receipt.photo_url,
        ingredients=receipt.ingredients,
        preparation_steps=receipt.preparation_steps,
        tags=receipt.tags,
        date_added=receipt.date_added,
        date_cooked=receipt.date_cooked,
        rating=receipt.rating
    )
    
    db.add(db_receipt)
    db.commit()
    db.refresh(db_receipt)
    return db_receipt


@app.get("/receipts/", response_model=List[schemas.Receipt])
def read_receipts(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    # Query the SQLAlchemy model from the database
    receipts = db.query(models.Receipt).offset(skip).limit(limit).all()

    # Return the queried result (FastAPI will use the Pydantic model for response)
    return receipts

@app.put("/receipts/{receipt_id}/cooked")
def mark_as_cooked(receipt_id: int, db: Session = Depends(get_db)):
    receipt = db.query(Receipt).filter(Receipt.id == receipt_id).first()
    if receipt is None:
        raise HTTPException(status_code=404, detail="Receipt not found")
    receipt.date_cooked = datetime.utcnow()
    db.commit()
    db.refresh(receipt)
    return receipt
