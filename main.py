from datetime import datetime
from typing import Union,Text,Optional
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4 as uuid
app = FastAPI()

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

@app.get("/ufos")
def get_ufos():
    return ufos_array

@app.post("/ufos")
def save_ufos(ufos:Ufo):
    ufos.id=str(uuid())
    ufos_array.append(ufos.dict())
    return ufos

@app.get('/ufos/{ufos_id}')
def get_ufos(ufos_id:str):
    for ufo in ufos_array:
        if ufo['id']==ufos_id:
            return ufo
    raise HTTPException(status_code=404.,detail="Ufo Not Found")


@app.delete("/ufos/{ufos_id}")
def delete_ufo(ufos_id:str):
    for index,ufo in enumerate(ufos_array):
        if ufo["id"]==ufos_id:
            ufos_array.pop(index)
            return {"message": "Ufo has been deleted successfully"}

    raise HTTPException(status_code=404.,detail="Ufo Not Found")

@app.put('/ufos/{ufo_id}')
def update_ufo(ufo_id:str,updateUfo:Ufo):
    for index,ufo in enumerate(ufos_array):
        if ufo['id']==ufo_id:
            ufos_array[index]["location_ufo"]=updateUfo.location_ufo
            ufos_array[index]["description"]=updateUfo.description
            ufos_array[index]["published"]=updateUfo.published
            return {"message": "Ufo has been Updated successfully"}
    raise HTTPException(status_code=404.,detail="Ufo Not Found")