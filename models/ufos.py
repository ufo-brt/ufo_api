from pydantic import BaseModel
from typing import Optional,List
from datetime import datetime



class Ufo(BaseModel):
    _id:Optional[str]
    date_time: Optional[datetime]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    city: str
    state: str
    country: str
    shape: str
    duration: int
    summary: str
    posted: str
    images:bool
    hoax:int