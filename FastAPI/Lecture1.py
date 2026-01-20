from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items")
def read_items(item_name : str , item_id : int):
    return {"item_name": item_name, "item_id": item_id}