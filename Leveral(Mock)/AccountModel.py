from sqlalchemy import Column, Integer, String, Date
from config import engine,Base
# from base import Base

class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    # cust_id = Column(String,ForeignKey("customer.cust_id"),nullable=False)
    cust_id = Column(String , nullable=False)
    balance = Column(Integer, default=0)
    acc_status = Column(String, default="active")

    # customer=relationship("Customer",back_populates="accounts")
    # transactions=relationship("Transaction",back_populates="account",cascade="all,delete")



Base.metadata.create_all(bind=engine)

