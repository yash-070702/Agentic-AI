# Import SQLAlchemy column types
from sqlalchemy import Column, Integer, String, DateTime, Text

# Used to set default date/time
from datetime import datetime

# Import Base class and engine from config
from config import Base, engine


# -------------------- USER MODEL --------------------
class User(Base):
    # Table name in database
    __tablename__ = "users"

    # Primary key column (auto-incremented)
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)

    # Username field (must be unique)
    username = Column(String, unique=True, index=True)


# -------------------- POST MODEL --------------------
class Post(Base):
    # Table name in database
    __tablename__ = "posts"

    # Primary key column
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)

    # Post title
    title = Column(String)

    # Username of the user who created the post
    # (Currently stored as string, not foreign key)
    username = Column(String, index=True)

    # Timestamp when post is created
    # Default is current UTC time
    created_at = Column(DateTime, default=datetime.utcnow)

    # Comments stored as JSON string
    # Example: ["Nice post!", "Awesome"]
    comments = Column(Text)


# Create all tables in database
# This will generate tables if they do not exist
Base.metadata.create_all(bind=engine)
