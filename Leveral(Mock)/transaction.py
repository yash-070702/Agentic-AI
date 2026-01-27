from fastapi import FastAPI,HTTPException,Depends
from sqlalchemy.orm import Session
from config import get_db
from typing import List
from Model import Account,Transaction
from accountSchema import AccountSchema
from transactionSchema import TransactionSchema, TransactionResponse

from datetime import date
import uvicorn

app=FastAPI(title="Leveral Mock Banking App")

@app.get("/transactions", response_model=List[TransactionResponse])
def get_trans(type:str=None,amount:int=None,date_from:date=None,date_to:date=None,db:Session=Depends(get_db)):
    query=db.query(Transaction)
    if type:
        query=query.filter(Transaction.txn_type==type)
    if amount:
        query=query.filter(Transaction.txn_amt==amount)
    if date_from:
        query=query.filter(Transaction.txn_date>=date_from)
    if date_to:
        query=query.filter(Transaction.txn_date<=date_to)
    transactions=query.all()
    return {"message":"Transactions fetched successfully","transactions":transactions}

@app.get("/transactions/{txn_id}",response_model=TransactionResponse)
def get_txn(txn_id:int,db:Session=Depends(get_db)):
    txn=db.query(Transaction).filter(Transaction.id==txn_id).first()
    if not txn:
        raise HTTPException(status_code=404,detail="Transaction not found")
    return {"message":"Transaction fetched successfully","transaction":txn}

@app.post("/transactions/{accountId}")
def add_transaction(accountId:int,transaction:TransactionSchema,db:Session=Depends(get_db)):
    acc=db.query(Account).filter(Account.id==accountId).first()

    if not acc:
        raise HTTPException(status_code=404,detail="Account not found")

    if acc.acc_status!="active":
        raise HTTPException(status_code=400,detail="Account is not active")

    if transaction.txn_type=="Deposit":
        acc.balance+=transaction.txn_amt
    
    if transaction.txn_type=="Withdrawal":
        if acc.balance<transaction.txn_amt:
            raise HTTPException(status_code=400,detail="Insufficient balance")
        acc.balance-=transaction.txn_amt

    new_transaction=Transaction(**transaction.__dict__)
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return {"message":"Transaction successful","new_balance":acc.balance,"Transaction_Details":transaction}

@app.get("/accounts/{accountId}/statements" ,  response_model=List[TransactionResponse])
def get_account_statements(accountId:int,from_date:date,to_date:date,db:Session=Depends(get_db)):
    acc=db.query(Account).filter(Account.id==accountId).first()
    if not acc:
        raise HTTPException(status_code=404,detail="Account not found")

    transactions=db.query(Transaction).filter(Transaction.acc_id==accountId,
                                              Transaction.txn_date>=from_date,
                                              Transaction.txn_date<=to_date).order_by(Transaction.txn_date).all()
    return {"message":"Account statements fetched successfully","transactions":transactions}

@app.get("/accounts/{accountId}/ministatements" , response_model=List[TransactionResponse])
def get_account_ministatements(accountId:int,db:Session=Depends(get_db)):
    acc=db.query(Account).filter(Account.id==accountId).first()
    if not acc:
        raise HTTPException(status_code=404,detail="Account not found")

    transactions=db.query(Transaction).filter(Transaction.acc_id==accountId).order_by(Transaction.txn_date.desc()).limit(10).all()
    return {"message":"Account mini statements fetched successfully","transactions":transactions}