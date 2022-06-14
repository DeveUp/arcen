from pydantic import BaseModel
from pydantic import EmailStr
from datetime import datetime


class UserResponse(BaseModel):
    id:int
    document: str
    full_name: str
    email : EmailStr
    password : str
    status : bool
    session_started: bool
    date: datetime

    class Config:
        orm_mode = True