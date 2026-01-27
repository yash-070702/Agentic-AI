from pydantic import EmailStr,Field, BaseModel
from typing import Optional
from datetime import date

class ProjectSchema(BaseModel):
    title:Optional[str]=Field(None,min_length=5)
    description:Optional[str]=Field(None,min_length=10)
    owner_id:Optional[int]=None
    created_at:Optional[date]=None

class ProjectResponse(BaseModel):
    id:int
    title:str
    description:str
    owner_id:int
    created_at:date

    class Config:
        from_attributes:True