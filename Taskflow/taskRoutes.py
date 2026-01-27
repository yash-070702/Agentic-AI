from fastapi import FastAPI,HTTPException,Depends
from config import get_db
from sqlalchemy.orm import Session
from Model import Task,Project
from TaskSchema import TaskSchema

app=FastAPI(title='Task Routes')

@app.post('/task/create_task/{projectId}')
def create_task(projectId:int,task:TaskSchema,db:Session=Depends(get_db)):
    project=db.query(Project).filter(Project.id==projectId).first()

    if not project:
        raise HTTPException(status_code=404 , detail="No such project exist")

    new_task=Task(**task.__dict__)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {"message":"task added successfully",
            "task":new_task}

@app.get("/task/all_tasks/{projectId}")
def get_task_project(projectId:int,db:Session=Depends(get_db)):
    project=db.query(Project).filter(Project.id==projectId).first()

    if not project:
        raise HTTPException(status_code=404 , detail="No such project exist")

    tasks=db.query(Task).filter(Task.project_id==projectId).all()

    return {"message":"task fetched successfully",
            "task":tasks}


@app.patch("/task/update_task/{taskId}")
def update_task(taskId:int,task:TaskSchema , db:Session=Depends(get_db)):
    exist_task=db.query(Task).filter(Task.id==taskId).first()

    if not exist_task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task.is_completed:
        exist_task.is_completed=task.is_completed
    
    db.commit()
    db.refresh(exist_task)

    return {"message":"task updated successfully",
            "task":exist_task}