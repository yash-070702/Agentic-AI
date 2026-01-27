from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal,List
from accountSchema import AccountSchema

class CustomerSchema(BaseModel):
    cust_id:str
    cust_name: Optional[str] = Field(None, min_length=4, max_length=15)
    cust_type: Optional[Literal["Regular", "Privileged"]] = None
    email: Optional[EmailStr] = None
    location: Optional[str] = None


class CustomerResponse(BaseModel):
    cust_id: str
    cust_name: str
    cust_type: str
    email: EmailStr
    location: str

    class Config:
        from_attributes = True
