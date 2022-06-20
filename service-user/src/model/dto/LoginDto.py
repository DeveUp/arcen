from pydantic import EmailStr
from pydantic import BaseModel

class LoginDto(BaseModel):
    document: str
    email : EmailStr
    password : str
