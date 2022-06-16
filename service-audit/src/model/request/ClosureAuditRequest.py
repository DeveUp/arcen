from pydantic import BaseModel

class ClosureAuditRequest(BaseModel):
    control: str
    audit: dict
    date:str
