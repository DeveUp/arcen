from pydantic import BaseModel

class TypeFurnitureDto(BaseModel):
    number_type_furniture: str
    count_rack: int
    count_row: int
    depth: int
    height: int
    width: int
    date: str