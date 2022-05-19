from pydantic import BaseModel

class BlockDto(BaseModel):
    letter: str
    flat: str
    date: str