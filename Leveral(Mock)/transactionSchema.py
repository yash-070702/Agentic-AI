from pydantic import BaseModel,field_validator
from datetime import date
from typing import Optional,Literal

class TransactionSchema(BaseModel):
    txn_type: Optional[Literal['Withdrawal','Deposit']]
    txn_amt: Optional[int]
    txn_date: Optional[date]
    acc_id: Optional[int]

    @field_validator('txn_date')
    def check_date(cls,value:Optional[date]):
        if value is None:
            return value

        if value<date.today():
            raise ValueError("date cant be of past")
        
        return value

class TransactionResponse(BaseModel):
    id: int
    txn_type: str
    txn_amt: int
    txn_date: date
    acc_id: int

    class Config:
        from_attributes = True


for col in nums_col:
    q1=df[col].quantile(0.25)
    q2=df[col].quantile(0.75)

    IQR=q2-q1

    lower=q1-1.5*IQR
    upper=q2+1.5*IQR

    df=df[(df[col]>=lower) & (df[col]<=upper)]

import seaborn as sns
import matplotlib.pyplot as plt

x = [1, 19, 10, 12, 13, 4, 5]

fig, ax = plt.subplots(figsize=(8,3))
sns.kdeplot(x, ax=ax)
plt.show()
