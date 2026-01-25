from sqlalchemy import Column, Integer, String, Date
from config import engine,Base
from sqlalchemy.orm import relationship
# from base import Base

class Customer(Base):
    __tablename__ = "customer"

    cust_id=Column(String,primary_key=True, index=True)
    cust_name = Column(String, nullable=True)
    cust_type = Column(String, unique=True)
    email = Column(String, unique=True)
    location = Column(String)

    # accounts=relationship("Account",back_populates="customer",cascade="all,delete")



   

Base.metadata.create_all(bind=engine)
