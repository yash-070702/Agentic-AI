from sqlalchemy import Column, Integer, String, Date
from config import Base, engine


class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    cust_name = Column(String, nullable=True)
    cust_type = Column(String, unique=True)
    email = Column(String, unique=True)
    location = Column(String)



Base.metadata.create_all(bind=engine)
