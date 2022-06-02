from pydantic import BaseModel

class TypeFurnitureResponse(BaseModel):
    id:int
    number_type_furniture: int
    count_rack: int
    count_row: int
    depth: int
    height: int
    width: int
    date:str