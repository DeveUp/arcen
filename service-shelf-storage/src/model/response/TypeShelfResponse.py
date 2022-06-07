from pydantic import BaseModel

class TypeShelfResponse(BaseModel):
    id: int
    number_type_shelf: int
    depth: int
    height: int
    width: int