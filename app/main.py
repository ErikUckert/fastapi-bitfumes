from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"data":{"name":"Erik",
                    "Age":20}}
    
@app.get("/about")
def about():
    return {"data":"About Page"}