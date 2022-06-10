from pydantic import BaseModel

class TypeBoxfDto(BaseModel):
    number_type_box: int
    depth: int
    height: int
    width: int