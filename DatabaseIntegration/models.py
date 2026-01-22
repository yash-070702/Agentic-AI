from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from config import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    username = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    comments = Column(Text)  # JSON array stored as string


    