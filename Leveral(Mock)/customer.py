from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from config import get_db
from CustomerModel import Customer
from AccountModel import Account
from customerSchema import CustomerSchema
from accountSchema import  AccountSchema
import uvicorn

app = FastAPI(title="Customer routes")


# -------------------- CREATE CUSTOMER --------------------
@app.post("/customers")
def add_customer(
    customer: CustomerSchema,
    db: Session = Depends(get_db)
):
    new_cust = Customer(**customer.__dict__)

    if db.query(Customer).filter(Customer.email == new_cust.email).first():
        raise HTTPException(
            status_code=400,
            detail="email already exist"
        )

    db.add(new_cust)
    db.commit()
    db.refresh(new_cust)

    return {"message": "customer added successfully"}


# -------------------- FETCH ALL CUSTOMERS --------------------
@app.get("/customers")
def fetch_cust(db: Session = Depends(get_db)):
    all_cust = db.query(Customer).all()
    result=[]

    for cust in all_cust:
        acc=db.query(Account).filter(Account.cust_id==cust.cust_id).all()
        result.append({"cust_name":cust.cust_name,
                        "cust_id":cust.cust_id,
                        "cust_acc":acc})

        

    return {
        "message": "all customer fetch successfully",
        "data": result
    }


# -------------------- FETCH CUSTOMER BY ID --------------------
@app.get("/customers/{custId}")
def fetch_a_user(custId: str, db: Session = Depends(get_db)):
    cust = db.query(Customer).filter(Customer.cust_id == custId).first()

    if not cust:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )
    acc=db.query(Account).filter(Account.cust_id==cust.cust_id).all()

    return {
        "message": "User fetched successfully",
        "user": {"data":cust,"accounts":acc}
        
    }


# -------------------- FETCH ACTIVE ACCOUNTS OF CUSTOMER --------------------
@app.get("/customers/{custId}/accounts")
def fetch_all_acc(custId: str, db: Session = Depends(get_db)):
    accounts = db.query(Account).filter(
        Account.cust_id == custId,
        Account.acc_status == "active"
    ).all()

    if not accounts:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    return {
        "message": "Accounts fetched successfully",
        "accounts": accounts
    }


# -------------------- UPDATE CUSTOMER --------------------
@app.patch("/customers/{custId}")
def update_customer(
    custId: str,
    customer: CustomerSchema,
    db: Session = Depends(get_db)
):
    update_cust = db.query(Customer).filter(Customer.cust_id == custId).first()

    if not update_cust:
        raise HTTPException(
            status_code=404,
            detail="no such customer"
        )

    if customer.email:
        update_cust.email = customer.email

    db.commit()
    db.refresh(update_cust)

    return {
        "message": "Customer updated successfully",
        "user": update_cust
    }


# -------------------- RUN SERVER --------------------
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
