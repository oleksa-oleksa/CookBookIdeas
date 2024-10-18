from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables from .env only if not in GitHub Actions
# The environment variable GITHUB_ACTIONS is automatically set to true inside GitHub Actions environments. 
# This environment variable will only exist when the code is being run in GitHub Actions.
if not os.getenv("GITHUB_ACTIONS"):
    # If it does not exist (meaning the code is running locally), 
    # the condition if not os.getenv("GITHUB_ACTIONS") will evaluate to True, 
    # and load_dotenv() will be called to load environment variables from the local .env file.
    load_dotenv()  # Only for local development

# Common logic for both environments
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# For GitHub Actions, these will be set in the Actions Secrets
# For local development, they'll be loaded from .env
DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency for getting a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
