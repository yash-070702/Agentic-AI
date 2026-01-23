from pydantic import BaseModel
from datetime import date
from typing import Optional,Literal

class TransactionSchema(BaseModel):
    txn_type: Optional[Literal['Withdrawal','Deposit']]
    txn_amt: Optional[int]
    txn_date: Optional[date]
    acc_id: Optional[int]