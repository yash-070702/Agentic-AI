from sqlalchemy import Column, Integer, String, Date
from config import Base, engine


class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    txn_type = Column(String)
    txn_amt = Column(Integer)
    txn_date = Column(Date)
    acc_id = Column(Integer)


Base.metadata.create_all(bind=engine)