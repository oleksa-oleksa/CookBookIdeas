from sqlalchemy import Column, Integer, String, Date, Text
from sqlalchemy.dialects.postgresql import ARRAY
from app.database import Base

class Receipt(Base):
    __tablename__ = "receipts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    photo = Column(String, nullable=True)
    ingredients = Column(ARRAY(String))
    preparation_steps = Column(Text)
    tags = Column(ARRAY(String))
    date_added = Column(Date)
    date_cooked = Column(Date, nullable=True)
    rating = Column(Integer, nullable=True)
