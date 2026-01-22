from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from config import get_db
from models import User, Post
from schemma import UserSchema, PostSchema
import json

app = FastAPI(title="Mini Insta App")

@app.post("/users/add")
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    new_user = User(**user.__dict__)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully", "user": new_user}


@app.post("/posts/add")
def create_post(post: PostSchema, db: Session = Depends(get_db)):
    new_post = Post(
        title=post.title,
        username=post.username,
        comments=json.dumps(post.comments)
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"message": "Post created successfully", "post": new_post}


@app.get("/posts")
def get_all_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return posts


@app.get("/posts/{post_id}")
def get_post_by_id(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@app.get("/posts/by-user")
def get_posts_by_username(username: str, db: Session = Depends(get_db)):
    posts = db.query(Post).filter(Post.username == username).all()
    return posts


@app.put("/posts/update-title/{post_id}")
def update_post_title(post_id: int, title: str, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    post.title = title
    db.commit()
    db.refresh(post)
    return {"message": "Post updated", "post": post}


@app.put("/posts/add-comment/{post_id}")
def add_comment(post_id: int, comment: str, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    comments = json.loads(post.comments)
    comments.append(comment)
    post.comments = json.dumps(comments)

    db.commit()
    db.refresh(post)
    return {"message": "Comment added", "post": post}


@app.delete("/posts/delete/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    db.delete(post)
    db.commit()
    return {"message": "Post deleted"}


@app.delete("/posts/delete-all")
def delete_all_posts(db: Session = Depends(get_db)):
    db.query(Post).delete()
    db.commit()
    return {"message": "All posts deleted"}


@app.patch("/posts/{post_id}")
def patch_post(
    post_id: int,
    post: PostSchema,
    db: Session = Depends(get_db)
):
    db_post = db.query(Post).filter(Post.id == post_id).first()

    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    # PATCH logic (manual)
    if post.title:
        db_post.title = post.title

    if post.username:
        db_post.username = post.username

    if post.comments:
        db_post.comments = json.dumps(post.comments)

    db.commit()
    db.refresh(db_post)

    return {"message": "Post partially updated", "post": db_post}