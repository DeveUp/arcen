from pydantic import BaseModel

class BlockRequest(BaseModel):
    id: int
    letter: str
    flat: str
    date: str