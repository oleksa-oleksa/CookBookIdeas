from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class ReceiptBase(BaseModel):
    title: str
    photo: Optional[str] = None  # This can be a URL or a path
    ingredients: List[str]
    preparation_steps: str
    tags: List[str]
    date_added: date
    date_cooked: Optional[date] = None
    rating: Optional[int] = None

class ReceiptCreate(ReceiptBase):
    pass

class Receipt(ReceiptBase):
    id: int

    class Config:
        orm_mode = True  # This allows SQLAlchemy models to be converted to Pydantic models
