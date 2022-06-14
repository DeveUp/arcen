from pydantic import EmailStr
from pydantic import BaseModel

class UserDto(BaseModel):
    document: str
    full_name: str
    email : EmailStr
    password : str
