from pydantic import BaseModel

class FurnitureResponse(BaseModel):
    id:int
    id_block: int
    id_type_furniture: int
    number_furniture: int
    date:str