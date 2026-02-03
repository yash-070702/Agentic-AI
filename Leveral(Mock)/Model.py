from sqlalchemy import Column , Integer , String , Date , ForeignKey
from config import Base , engine 
from sqlalchemy.orm import relationship


class Customer(Base):

    __tablename__='customer'
    cust_id=Column(String , primary_key=True,index=True)
    cust_name=Column(String , nullable=False)
    cust_type=Column(String , nullable=False)
    email=Column(String , unique=True, nullable=False)
    location=Column(String)

    accounts=relationship('Account', back_populates='customer', cascade='all,delete')


class Account(Base):
     __tablename__ = "account" 
     id = Column(Integer, primary_key=True, autoincrement=True, index=True) 
     cust_id = Column(String , ForeignKey('customer.cust_id'),nullable=False) 
     balance = Column(Integer, default=0) 
     acc_status = Column(String, default="active")

     customer=relationship('Customer',back_populates='accounts')
     transactions=relationship('Transaction', back_populates='account',cascade='all,delete')

class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    acc_id = Column(Integer, ForeignKey("account.id"), nullable=False)
    tax_type = Column(String)
    tax_amt = Column(Integer)
    tax_date = Column(Date)

    account=relationship('Account' ,back_populates='transactions')

    @

Base.metadata.create_all(bind=engine)