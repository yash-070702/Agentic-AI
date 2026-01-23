from sqlalchemy import Column, Integer, String, Date
from config import Base, engine

class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    cust_id = Column(String)
    balance = Column(Integer, default=0)
    acc_status = Column(String, default="active")


Base.metadata.create_all(bind=engine)