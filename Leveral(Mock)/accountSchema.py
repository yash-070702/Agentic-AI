from pydantic import BaseModel, EmailStr, Field
from typing import Literal,Optional

class AccountSchema(BaseModel):
    cust_id: Optional[str] = None
    balance: Optional[float] = Field(None, gt=0, le=9999999)
    acc_status: Optional[Literal["active", "inactive"]] = None

class AccountResponse(BaseModel):
    id: int
    cust_id: int
    balance: float
    acc_status: str

    class Config:
        from_attributes = True
