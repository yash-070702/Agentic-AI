from pydantic import BaseModel
from datetime import datetime
from typing import List


class UserSchema(BaseModel):
    id: int
    username: str


class PostSchema(BaseModel):
    id: int
    title: str
    username: str
    created_at: datetime
    comments: List[str]
