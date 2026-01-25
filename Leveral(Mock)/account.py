from fastapi import FastAPI , HTTPException , Depends
from sqlalchemy.orm import Session
from config import get_db
from AccountModel import Account
from CustomerModel import Customer

from accountSchema import AccountSchema
import uvicorn

app = FastAPI(title="Account routes")

# -------------------- CREATE ACCOUNT --------------------
@app.post("/accounts")
def new_acc(custId:str,db:Session=Depends(get_db)):
    cust=db.query(Customer).filter(Customer.cust_id==custId).first()

    if not cust:
        raise HTTPException(statrus_code=404,detail="Customer Not Found")

    new_acc=Account(cust_id=custId)
    db.add(new_acc)
    db.commit()
    db.refresh(new_acc)

    return {"message":"Account created successfully","account":new_acc}

# -------------------- FETCH ALL ACCOUNTS --------------------
@app.get("/accounts")
def get_active_acc(db:Session=Depends(get_db)):
    all_acc=db.query(Account).filter(Account.acc_status=="active").all()

    if not all_acc:
        raise HTTPException(status_code=404,detail="No Active Accounts Found")

    return {"message":"All active accounts fetched successfully","data":all_acc}

# -------------------- FETCH ACCOUNT BY ID --------------------
@app.get("/accounts/{accountId}")
def get_acc_by_id(accountId:int,db:Session=Depends(get_db)):
    acc=db.query(Account).filter(Account.id==accountId).first()

    if not acc:
        raise HTTPException(status_code=404,detail="Account Not Found")
    
    if acc.status=="inactive":
        raise HTTPException(status_code=400,detail="sorry account is inactive")

    return {"message":"Account Details fetched successfully",
    "account":acc}


# -------------------- DELETE ACCOUNT BY ID --------------------
@app.delete("/accounts/{accountId}")
def del_acc_by_id(accountId:int,db:Session=Depends(get_db)):
    acc=db.query(Account).filter(Account.id==accountId).first()

    if not acc:
        raise HTTPException(status_code=404,detail="Account Not Found")

    acc.acc_status="inactive"
    db.commit()
    return {"message":"Account deleted successfully"}

# -------------------- FETCH ACCOUNT BALANCE --------------------
@app.get("/accounts/{accountId}/balance")
def get_acc_balance(accountId:int,db:Session=Depends(get_db)):
    acc=db.query(Account).filter(Account.id==accountId).first()

    if not acc:
        raise HTTPException(status_code=404,detail="Account Not Found")

    if acc.acc_status=="inactive":
        raise HTTPException(status_code=400,detail="sorry account is inactive")

    return {"message":"Account balance fetched successfully",
    "balance":acc.balance}


# -------------------- UPDATE ACCOUNT BALANCE --------------------
@app.patch("/accounts/{accountId}")
def update_acc_balance(accountId:int,account:AccountSchema,db:Session=Depends(get_db)):
    acc=db.query(Account).filter(Account.id==accountId).first()
    if not acc:
        raise HTTPException(status_code=404,detail="Account Not Found")

    if account.balance < 0:
        raise HTTPException(status_code=400,detail="Balance cannot be negative")
    
    if account.balance is not None:
        acc.balance=account.balance
    db.commit()
    db.refresh(acc)
    return {"message":"Account balance updated successfully",
    "account":acc}

