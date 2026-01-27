from fastapi import FastAPI,HTTPException ,Depends
from config import get_db
from Model import Project
from sqlalchemy.orm import Session
from ProjectSchema import ProjectSchema
from Model import User , Project

app=FastAPI(title="Project Routes")
@app.post("/project/createProject/{userId}")
def create_project(userId:int,project:ProjectSchema,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.id==userId).first()

    if not user:
        raise HTTPException(status_code=404,detail="No such User Exist")

    new_project=Project(**project.__dict__)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return {"message":"Project Added Successfully",
            "project":new_project}

@app.get("/project/getAllProjects")
def get_all_projects(db:Session=Depends(get_db)):
    projects=db.query(Project).all()

    return {"message":"projects fetched successfully",
            "projects":projects}

@app.get("/projects/user/{userId}")
def project_of_user(userId:int,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.id==userId).first()

    if not user:
        raise HTTPException(status_code=404,detail="No such User Exist")

    projects=db.query(Project).filter(Project.owner_id==userId).all()

    return {"message":"fetched all projects of user sucessfully",
            "projects":projects}

@app.patch("/project/update_project/{projectId}")
def update_project(projectId:int,project:ProjectSchema,db:Session=Depends(get_db)):
    exist_project=db.query(Project).filter(Project.id==projectId).first()

    if not exist_project:
        raise HTTPException(status_code=404,detail="No such project avalaible")
    
    if project.title:
        exist_project.title=project.title
    
    if project.description:
        exist_project.description=project.description
    
    db.commit()
    db.refresh(exist_project)

    return {"message":"Project updated successfully",
            "project":exist_project}
