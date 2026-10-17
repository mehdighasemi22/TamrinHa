
from fastapi import FastAPI, HTTPException

app = FastAPI()

#-------------------------------------------------------------------------------

@app.get("/")
def home():
    return {"message": "Welcome to my calculator API!"}



@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}



@app.get("/subtract")
def subtract(a: float, b: float):
    return {"result": a - b}



@app.get("/multiply")
def multiply(a: float, b: float):
    return {"result": a * b}




@app.get("/power")
def power(a: float, b: float):
    return {"result": a ** b}




@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(
            status_code=400,
            detail="Cannot divide by zero"
        )

    return {"result": a / b}

