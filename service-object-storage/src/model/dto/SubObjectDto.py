from pydantic import BaseModel

class SubObjectDto(BaseModel):
    number: int
    box: int