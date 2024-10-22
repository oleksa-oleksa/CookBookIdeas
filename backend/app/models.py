from sqlalchemy import Column, Integer, String, Date, Text
from sqlalchemy.dialects.postgresql import ARRAY
from app.database import Base
from sqlalchemy.dialects.postgresql import JSON

class Receipt(Base):
    """
    SQLAlchemy Receipt: This represents the structure of the data in your database.
    It defines the receipts table with columns like id, title, ingredients, etc.

    The receipts table is created inside the receipts_db database, 
    and it contains all the columns like id, title, photo, ingredients, etc.

    POSTGRES_DB=receipts_db:
    This defines the database (or container) that PostgreSQL will use to store application's data.
    It's configured in the .env file because it needs to be passed to FastAPI app and database
    configuration to connect to the correct PostgreSQL database.

    receipts table:
    This table is created inside the receipts_db database. 
    The table holds an application's actual data—each row corresponds to a receipt
    and contains information such as title, ingredients, photo, and other fields.
    """
    __tablename__ = "receipts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    photo_url = Column(String, nullable=True)
    ingredients = Column(JSON)
    preparation_steps = Column(ARRAY(String))  # Store each step as a separate string
    tags = Column(ARRAY(String))
    date_added = Column(Date)
    date_cooked = Column(Date, nullable=True)
    rating = Column(Integer, nullable=True)
    default_servings = Column(Integer, nullable=False) 
