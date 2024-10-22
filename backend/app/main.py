from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, database, schemas
from app.schemas import ReceiptCreate
from app.models import Receipt
from app.database import get_db
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from app.helpers.utils import scale_ingredients

app = FastAPI()

# Allow CORS for Angular's development server (localhost:4200)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # List the allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Create the database tables when the application starts if they don't exist.
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
    """
    Create an instance of the SQLAlchemy model
    ReceiptCreate for data input validation when creating new receipts (via POST).
    
    The receipt parameter is coming from the request body, 
    and FastAPI is automatically validating and parsing it as an instance 
    of the ReceiptCreate Pydantic model.

    Pydantic Model (ReceiptCreate): The receipt is expected to match the structure 
    of the ReceiptCreate class, which is defined in schemas.py.
    This Pydantic model is used to validate and parse the incoming request data
    (like title, photo, ingredients, etc.).

    Request Body Parsing: When a client makes a POST request to this endpoint,
    the data in the request body (usually in JSON format) is automatically
    parsed by FastAPI into an instance of the ReceiptCreate model. 
    FastAPI does this by inspecting the type hint (ReceiptCreate) in the function definition.

    In the request body, the receipt parameter will appear as a JSON object 
    that matches the structure defined in the ReceiptCreate Pydantic model.
    When a client sends a POST request to the  /receipts/ endpoint, they will provide the data in this format.

    When a Pydantic model as a function parameter, the data comes from the body of the request. 
    Pydantic models (like ReceiptCreate) are automatically interpreted as request body inputs by FastAPI.
    When a Pydantic model is used in an endpoint function parameter, 
    FastAPI knows to expect that the client will send this data in the body of the request as JSON.

    """
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
    # Query the receipt from the database
    receipt = db.query(models.Receipt).filter(models.Receipt.id == receipt_id).first()
    
    # If receipt is not found, raise an HTTP 404 error
    if receipt is None:
        raise HTTPException(status_code=404, detail="Receipt not found")
    
    # Set the current date and time for 'date_cooked'
    receipt.date_cooked = datetime.now()
    
    # Commit the changes to the database and refresh the receipt
    db.commit()
    db.refresh(receipt)
    
    return receipt
