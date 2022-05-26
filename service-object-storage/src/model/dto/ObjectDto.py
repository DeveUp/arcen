from pydantic import BaseModel

class ObjectDto(BaseModel):
    id_type_object: int
    id_sub_object: int