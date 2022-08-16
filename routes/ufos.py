from fastapi import APIRouter,HTTPException
from datetime import datetime
from typing import Union,Text,Optional
from uuid import uuid4 as uuid

ufo=APIRouter()
ufos_array=[]

@ufo.get("/ufos")
def get_ufos():
    return ufos_array

@ufo.get("/ufos")
def get_ufos():
    return ufos_array

@ufo.post("/ufos")
def save_ufos(ufos:Ufo):
    ufos.id=str(uuid())
    ufos_array.append(ufos.dict())
    return ufos

@ufo.get('/ufos/{ufos_id}')
def get_ufos(ufos_id:str):
    for ufo in ufos_array:
        if ufo['id']==ufos_id:
            return ufo
    raise HTTPException(status_code=404.,detail="Ufo Not Found")


@ufo.delete("/ufos/{ufos_id}")
def delete_ufo(ufos_id:str):
    for index,ufo in enumerate(ufos_array):
        if ufo["id"]==ufos_id:
            ufos_array.pop(index)
            return {"message": "Ufo has been deleted successfully"}

    raise HTTPException(status_code=404.,detail="Ufo Not Found")

@ufo.put('/ufos/{ufo_id}')
def update_ufo(ufo_id:str,updateUfo:Ufo):
    for index,ufo in enumerate(ufos_array):
        if ufo['id']==ufo_id:
            ufos_array[index]["location_ufo"]=updateUfo.location_ufo
            ufos_array[index]["description"]=updateUfo.description
            ufos_array[index]["published"]=updateUfo.published
            return {"message": "Ufo has been Updated successfully"}
    raise HTTPException(status_code=404.,detail="Ufo Not Found")