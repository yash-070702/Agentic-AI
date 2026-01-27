from fastapi import FastAPI,HTTPException,Depends
from sqlalchemy.orm import Session 
from config import get_db
from Model import User
from typing import List
from UserSchema import UserSchema,UserResponse
from Model import User,Project

app=FastAPI(title='Routes for User',response_model=UserResponse)

@app.post("/user/create_user")
def create_user(user:UserSchema,db:Session=Depends(get_db)):
    reg_user=db.query(User).filter(User.email==user.email).first()

    if reg_user:
        raise HTTPException(status_code=400 , detail="User with email exist")

    new_user=User(**user.__dict__)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message":"User Created Successfully",
            "User":new_user}

@app.get("/user/all_user")
def all_users(db:Session=Depends(get_db)):

    list_user=[]
    users=db.query(User).all()

    for user in users:
        user_id=user.id
        user_dict={}

        projects=db.query(Project).filter(Project.owner_id==user_id).all()
        user_dict['user']=user
        user_dict['projects']=projects
        list_user.append(user_dict)

    return {"message":"all users fetched",
            "users":list_user}

@app.get("/user/{user_id}")
def get_user(user_id:int,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.id==user_id).first()

    if not user:
        raise HTTPException(status_code=404,detail="User with id not found")

    projects=db.query(Project).filter(Project.owner_id==user_id).all()
    user_dict={}
    user_dict['user']=user
    user_dict['projects']=projects

    return {"message":"user fetched successfully",
            "user":user_dict}

@app.patch("/user/{user_id}")
def get_user(user_id:int,user:UserSchema,db:Session=Depends(get_db)):
    exist_user=db.query(User).filter(User.id==user_id).first()

    if not exist_user:
        raise HTTPException(status_code=404,detail="User with id not found")

    if user.name:
        exist_user.name=user.name
    
    if user.is_active:
        exist_user.is_active=user.is_active

    db.commit()
    db.refresh(exist_user)

    return {"message":"user updated successfully",
            "user":exist_user}



