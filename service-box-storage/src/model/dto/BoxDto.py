from unicodedata import name
from pydantic import BaseModel

class BoxDto(BaseModel):
    id_tray: int
    id_type_box: int
    number_box : int