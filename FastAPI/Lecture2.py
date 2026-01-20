from fastapi import FastAPI
import uvicorn 
from fastapi.responses import HTMLResponse

app = FastAPI()
@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <h1>Hello, World!</h1>
    """

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)
    