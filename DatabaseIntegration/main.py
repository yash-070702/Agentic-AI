# Import FastAPI framework and required dependencies
from fastapi import FastAPI, Depends, HTTPException

# Import SQLAlchemy Session to interact with DB
from sqlalchemy.orm import Session

# Import database dependency
from config import get_db

# Import SQLAlchemy models
from models import User, Post

# Import Pydantic schemas (for request validation)
from schemma import UserSchema, PostSchema

# Used to convert comments list <-> JSON string
import json


# Create FastAPI app instance
app = FastAPI(title="Mini Insta App")


# -------------------- USER APIs --------------------

# Create a new user
@app.post("/users/add")
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    # Convert Pydantic schema to SQLAlchemy model
    new_user = User(**user.__dict__)

    # Add user to DB
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully", "user": new_user}


# Get all users
@app.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()


# Get user by ID
@app.get("/users/{user_id}")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    # Fetch user from DB
    user = db.query(User).filter(User.id == user_id).first()

    # If user does not exist
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


# Get user by username (query parameter)
@app.get("/users/by-name/{username}")
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


# Update username using PUT (full update)
@app.put("/users/update/{user_id}")
def update_user(user_id: int, username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Update username
    user.username = username
    db.commit()
    db.refresh(user)

    return {"message": "User updated", "user": user}


# Partial update user using PATCH
@app.patch("/users/{user_id}")
def patch_user(user_id: int, user: UserSchema, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Update only provided fields
    if user.username:
        db_user.username = user.username

    db.commit()
    db.refresh(db_user)

    return {"message": "User partially updated", "user": db_user}


# Delete user by ID
@app.delete("/users/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return {"message": "User deleted"}


# Delete all users
@app.delete("/users/delete-all")
def delete_all_users(db: Session = Depends(get_db)):
    db.query(User).delete()
    db.commit()

    return {"message": "All users deleted"}


# -------------------- POST APIs --------------------

# Create a new post
@app.post("/posts/add")
def create_post(post: PostSchema, db: Session = Depends(get_db)):
    # Store comments as JSON string
    new_post = Post(
        title=post.title,
        username=post.username,
        comments=json.dumps(post.comments)
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return {"message": "Post created successfully", "post": new_post}


# Get all posts
@app.get("/posts")
def get_all_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()


# Get post by ID
@app.get("/posts/{post_id}")
def get_post_by_id(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return post


# Get all posts by username
@app.get("/posts/by-user")
def get_posts_by_username(username: str, db: Session = Depends(get_db)):
    return db.query(Post).filter(Post.username == username).all()


# Update post title
@app.put("/posts/update-title/{post_id}")
def update_post_title(post_id: int, title: str, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    post.title = title
    db.commit()
    db.refresh(post)

    return {"message": "Post updated", "post": post}


# Add a new comment to a post
@app.put("/posts/add-comment/{post_id}")
def add_comment(post_id: int, comment: str, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    # Convert JSON string back to list
    comments = json.loads(post.comments)
    comments.append(comment)

    # Save back as JSON string
    post.comments = json.dumps(comments)

    db.commit()
    db.refresh(post)

    return {"message": "Comment added", "post": post}


# Delete post by ID
@app.delete("/posts/delete/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    db.delete(post)
    db.commit()

    return {"message": "Post deleted"}


# Delete all posts
@app.delete("/posts/delete-all")
def delete_all_posts(db: Session = Depends(get_db)):
    db.query(Post).delete()
    db.commit()

    return {"message": "All posts deleted"}


# Partial update post using PATCH
@app.patch("/posts/{post_id}")
def patch_post(post_id: int, post: PostSchema, db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()

    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    # Update only provided fields
    if post.title:
        db_post.title = post.title

    if post.username:
        db_post.username = post.username

    if post.comments:
        db_post.comments = json.dumps(post.comments)

    db.commit()
    db.refresh(db_post)

    return {"message": "Post partially updated", "post": db_post}
