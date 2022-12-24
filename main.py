import numpy as np
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"),name="static")

@app.get("/")
def greet(request: Request):
    return templates.TemplateResponse("welcome.html",{"request":request})

@app.get('/solve/{ma1}/{ma2}')
def linalgSolve(request: Request,ma1:str,ma2:str):
    matrix1 = json.loads(ma1)
    matrix2 = json.loads(ma2)
    A = np.matrix(matrix1)
    B = np.matrix(matrix2)
    X0 = np.linalg.solve(A,B)
    X1 = X0.tolist()
    for i,j in enumerate(X1):
        X1[i][0] = round(j[0],1)
    return templates.TemplateResponse("solution.html",{"request":request,"X":X1})
