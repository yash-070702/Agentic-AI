from pydantic import BaseModel
from datetime import datetime
from typing import List


class UserSchema(BaseModel):
    username: str


class PostSchema(BaseModel):
    title: str
    username: str
    created_at: datetime
    comments: List[str]
