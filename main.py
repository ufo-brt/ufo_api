
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from routes.ufos import ufo
from uuid import uuid4 as uuid

app = FastAPI()
app.include_router(ufo)

ufos_array=[]



@app.get("/")
def read_root():
    return {"Wecome": "Welcome to my rest API"}

