from sqlalchemy import Column, Integer, String, DateTime, Float, Text, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Receipt(Base):
    __tablename__ = "receipts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    photo_url = Column(String, nullable=True)
    ingredients = Column(ARRAY(String), nullable=False)  # List of ingredients
    preparation_steps = Column(Text, nullable=False)
    tags = Column(ARRAY(String), nullable=True)  # List of tags (e.g., "meat", "veggie")
    date_added = Column(DateTime, default=datetime.utcnow)  # Auto set when added
    date_cooked = Column(DateTime, nullable=True)
    rating = Column(Float, nullable=True)  # Rating out of 5
