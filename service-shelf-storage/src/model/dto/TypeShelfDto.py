from pydantic import BaseModel

class TypeShelfDto(BaseModel):
    number_type_shelf: int
    depth: int
    height: int
    width: int
    date: str