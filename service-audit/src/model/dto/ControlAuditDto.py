from pydantic import BaseModel

class ControlAuditDto(BaseModel):
    name: str
    date_start: str
    date_end: str