from pydantic import BaseModel

class ControlAuditDto(BaseModel):
    id: str
    name: str
    date_start: str
    date_end: str
    date: str