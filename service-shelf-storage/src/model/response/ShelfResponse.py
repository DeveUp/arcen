from unicodedata import name
from pydantic import BaseModel

class ShelfResponse(BaseModel):
    id: int
    id_dependence: int
    id_type_shelf: int
    id_furniture: int
    number_shelf: int