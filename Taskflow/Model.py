from config import Base,engine
from sqlalchemy import Column , Integer , String ,Date , ForeignKey,Boolean,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__="user"
    id = Column(Integer,primary_key=True,autoincrement=True,index=True)
    name=Column(String,nullable=False)
    email=Column(String,unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    projects=relationship("Project",back_populates="owner" ,  cascade="all,delete")

class Project(Base):
    __tablename__="project"
    id = Column(Integer,primary_key=True,autoincrement=True,index=True)
    title=Column(String,nullable=False)
    description=Column(String)
    owner_id=Column(Integer , ForeignKey('user.id') , nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    owner=relationship("User" , back_populates='projects')
    tasks=relationship("Task" , back_populates='project' ,  cascade='all,delete')

class Task(Base):
    __tablename__="task"
    id = Column(Integer,primary_key=True,autoincrement=True,index=True)
    title=Column(String,nullable=False)
    is_completed = Column(Boolean, default=False)
    project_id=Column(Integer,ForeignKey('project.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    project=relationship("Project", back_populates="tasks")


Base.metadata.create_all(bind=engine)
    

