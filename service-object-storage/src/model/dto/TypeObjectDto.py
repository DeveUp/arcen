from pydantic import BaseModel

class TypeObjectDto(BaseModel):
    name: str
    height: int
    width: int
    depth: int