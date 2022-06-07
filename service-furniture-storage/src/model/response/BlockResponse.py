from pydantic import BaseModel
from datetime import datetime

class BlockResponse(BaseModel):
    id: int
    letter: str
    flat: str
    date: datetime