from typing import List
from fastapi import APIRouter, HTTPException, Response,status
from config.db import conn
from schemas.ufo import ufoEntity, ufosEntity
from models.ufos import Ufo
from uuid import uuid4 as uuid
from bson import ObjectId
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_204_NO_CONTENT

ufo = APIRouter()

ufos_array = []


@ufo.get("/ufos",tags=["ufos"])
def get_all_ufos():
    return ufosEntity(conn.ufo_db.ufo_history.find().limit(50))


@ufo.post("/ufos",response_model=Ufo,tags=["ufos"])
def save_ufos(ufos: Ufo):
    new_ufo = dict(ufos)
    id = conn.ufo_db.ufo_history.insert_one(new_ufo).inserted_id
    return str(id)


@ufo.get('/ufos/{ufo_id}', response_model=Ufo, tags=["ufos"])
def get_ufo(ufo_id: str):
    try:
        ufo = conn.ufo_db.ufo_history.find_one({"_id": ObjectId(ufo_id)})
        if not ufo:
            raise Response(status_code=HTTP_404_NOT_FOUND)
        else:
            return ufoEntity(ufo)
    except Exception as e:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=str(e))


@ufo.put('/ufos/{ufo_id}', response_model=Ufo, tags=["ufos"])
def update_ufo(ufo_id: str, updateUfo: Ufo):
    try:
        conn.ufo_db.ufo_history.find_one_and_update(
            {"_id": ObjectId(ufo_id)}, {'$set': updateUfo})
        return ufoEntity(conn.ufo_db.ufo_history.find_one({"_id": ObjectId(ufo_id)}))
    except Exception as e:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=str(e))


@ufo.delete("/ufos/{ufos_id}",status_code=status.HTTP_204_NO_CONTENT,tags=["ufos"])
def delete_ufo(ufo_id: str):
    try:
        conn.ufo_db.ufo_history.find_one_and_delete({"_id": ObjectId(ufo_id)})
        return Response(status_code=HTTP_204_NO_CONTENT)
    except Exception as e:
        return HTTPException(status_code=HTTP_404_NOT_FOUND, detail=str(e))
