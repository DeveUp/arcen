from pydantic import BaseModel

class ClosureAuditDto(BaseModel):
    id: str
    date_start: str
    date_end: str