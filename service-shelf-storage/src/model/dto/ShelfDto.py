from unicodedata import name
from pydantic import BaseModel

class DependenceDto(BaseModel):
    id_dependence: int
    id_type_shelf: int
    id_furniture: int
    date: int