from unicodedata import name
from pydantic import BaseModel

class ShelfDto(BaseModel):
    id_dependence: int
    id_type_shelf: int
    id_furniture: int
    number_shelf: int
    date: str