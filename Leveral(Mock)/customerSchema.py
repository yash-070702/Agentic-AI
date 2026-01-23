from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal

class CustomerSchema(BaseModel):
    cust_name: Optional[str] = Field(None, min_length=4, max_length=15)
    cust_type: Optional[Literal["Regular", "Privileged"]] = None
    email: Optional[EmailStr] = None
    location: Optional[str] = None
