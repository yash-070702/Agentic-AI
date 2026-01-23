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

    return {
        "message": "all customer fetch successfully",
        "data": all_cust
    }


# -------------------- FETCH CUSTOMER BY ID --------------------
@app.get("/customers/{custId}")
def fetch_a_user(custId: int, db: Session = Depends(get_db)):
    cust = db.query(Customer).filter(Customer.id == custId).first()

    if not cust:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )

    return {
        "message": "User fetched successfully",
        "user": cust
    }


# -------------------- FETCH ACTIVE ACCOUNTS OF CUSTOMER --------------------
@app.get("/customers/{custId}/accounts")
def fetch_all_acc(custId: int, db: Session = Depends(get_db)):
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
    custId: int,
    customer: CustomerSchema,
    db: Session = Depends(get_db)
):
    update_cust = db.query(Customer).filter(Customer.id == custId).first()

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
