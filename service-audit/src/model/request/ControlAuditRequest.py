from pydantic import BaseModel

class ControlAuditRequest(BaseModel):
    name: str
    date_start: str
    date_end: str
    date:str