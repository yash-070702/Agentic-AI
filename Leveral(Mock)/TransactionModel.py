from sqlalchemy import Column, Integer, String, Date
from config import  engine,Base
# from base import Base

class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    txn_type = Column(String)
    txn_amt = Column(Integer)
    txn_date = Column(Date)
    # acc_id = Column(Integer,ForeignKey("account.id"),nullable=False)
    acc_id = Column(Integer ,nullable=False)
    # account=relationship("Account",back_populates="transactions")
Base.metadata.create_all(bind=engine)