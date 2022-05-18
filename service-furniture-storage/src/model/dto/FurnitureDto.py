from pydantic import BaseModel

class FurnitureDto(BaseModel):
    id_block: str
    id_type_furniture: str
    number_furniture: str
    creation_date: str