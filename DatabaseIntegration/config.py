# Import SQLAlchemy functions to create database engine
from sqlalchemy import create_engine

# Import tools to manage DB sessions and models
from sqlalchemy.orm import sessionmaker, declarative_base


# Database connection URL
# Using SQLite database stored in 'chatapp.db' file
DATABASE_URL = "sqlite:///chatapp.db"


# Create database engine
# check_same_thread=False is required for SQLite
# because FastAPI uses multiple threads
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


# Create a SessionLocal class
# Each request will get its own DB session
session = sessionmaker(
    bind=engine
)


# Base class for all SQLAlchemy models
# Every model will inherit from this Base
Base = declarative_base()


# Dependency function for FastAPI
# This provides a database session to API routes
def get_db():
    db = session()      # Create new DB session
    try:
        yield db        # Give session to API
    finally:
        db.close()      # Always close session after request
