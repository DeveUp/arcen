from pydantic import BaseModel

class ControlAudit(BaseModel):
    id:str
    name: str
    date_start: str
    date_end: str
    date:str