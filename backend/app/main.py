from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, database
from app.models import Receipt
from app.database import get_db
from datetime import datetime

app = FastAPI()

# Create the database tables
models.Base.metadata.create_all(bind=database.engine)

@app.post("/receipts/")
def create_receipt(receipt: models.Receipt, db: Session = Depends(get_db)):
    db.add(receipt)
    db.commit()
    db.refresh(receipt)
    return receipt

@app.get("/receipts/")
def get_receipts(db: Session = Depends(get_db)):
    receipts = db.query(Receipt).all()
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
