from pydantic import Field , BaseModel
from typing import Optional
from datetime import date

class TaskSchema(BaseModel):
    title:Optional[str]=Field(None,min_length=10)
    is_completed:Optional[bool]=None
    project_id:Optional[int]=None
    created_at:Optional[date]=None

class TaskResponse(BaseModel):
    id:int
    title:str
    is_completed:bool
    project_id:int
    created_at:date

    class Config:
        from_attributes:True