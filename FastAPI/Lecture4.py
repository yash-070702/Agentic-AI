from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str


app = FastAPI()

users_db = []

@app.post("/users")
def create_user(user:User):
    users_db.append(user)
    return {
        "message": "User created",
        "user": user
    }

@app.get("/users")
def get_users():
    return {
        "users": users_db
    }       

@app.get("/users/{user_id}")
def get_user(user_id:int):
    if user_id>=len(users_db) or user_id<0:
        return {"error": "User not found"}

    return {
        "user": users_db[user_id]      
    }

@app.put("/users/{user_id}")
def update_user(user_id:int, updated_user:User):
    if user_id>=len(users_db) or user_id<0:
        return {"error": "User not found"}

    users_db[user_id] = updated_user
    return {
        "message": "User updated",
        "user": updated_user
    }

@app.delete("/users/{user_id}")
def delete_user(user_id:int):
    if user_id>=len(users_db) or user_id<0:
        return {"error": "User not found"}

    deleted_user = users_db.pop(user_id)
    return {
        "message": "User deleted",
        "user": deleted_user
    }
