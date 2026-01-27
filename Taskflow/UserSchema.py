from pydantic import BaseModel , EmailStr , Field
from typing import Optional ,  Literal
from datetime import date

class UserSchema(BaseModel):
    name:Optional[str]=Field(None,min_length=4  , description="name must be of valid size")
    email:Optional[EmailStr]=None
    is_active:Optional[bool]=None
    created_at:Optional[date]=None

class UserResponse(BaseModel):
    id:int
    name:str
    email:str
    is_active:bool
    created_at:date

    class Config:
      from_attributes:True