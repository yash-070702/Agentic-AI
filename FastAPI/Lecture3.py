from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str


app = FastAPI()

@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created",
        "user": user
    }
