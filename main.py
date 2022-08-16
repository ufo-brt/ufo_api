
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from routes.ufos import ufo
from uuid import uuid4 as uuid

app = FastAPI()
app.include_router(ufo)

ufos_array=[]

class Ufo(BaseModel):
    id:Optional[str]
    location_ufo:str
    description: Text
    is_offer: Union[bool, None] = None
    created_at:datetime=datetime.now()
    published_at:Optional[datetime]
    published:bool=False


@app.get("/")
def read_root():
    return {"Wecome": "Welcome to my rest API"}

