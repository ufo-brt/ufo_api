
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from routes.ufos import ufo
from uuid import uuid4 as uuid
from docs import tags_routes

app = FastAPI(
    title="UFOs REST API",
    description="This REST-API is used to store and retrieve UFO sightings.",
    version="0.1.0",
    openapi_tags=tags_routes
)
app.include_router(ufo)

@app.get("/", tags=["root"])
def read_root():
    return {"This is ufo rest API": "please visit /ufos"}

