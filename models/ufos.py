from pydantic import BaseModel
from typing import Optional

class Ufo(BaseModel):
    id:Optional[str]
    name:str
    email: str
    password: str
