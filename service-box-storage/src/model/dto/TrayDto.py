from unicodedata import name
from pydantic import BaseModel

class TrayDto(BaseModel):
    id_shelf: int
    depth: int
    height: int
    width: int