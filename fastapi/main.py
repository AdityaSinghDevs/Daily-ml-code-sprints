from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()

class Tea(BaseModel): #data validation using pydantic, gotta learn more abt this
    id :int
    name : str
    origin : str

teas : List[Tea] = []


@app.get("/") #Using decorator for routes
def read_root():
    return {"message" : "welcome Y'all"}

@app.get("/teas")
def get_teas():
    return teas


@app.post("/teas")
def add_tea(tea : Tea): #defined data type using pydantic

    teas.append(tea)
    return tea

@app.put("/teas/{tea_id}")
def update_tea(tea_id : int, updated_tea  :Tea): #creatinng normal functions then 

    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = update_tea
            return update_tea
    
    return {"error" : "Tea not found"}

