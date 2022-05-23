from pydantic import BaseModel

class ClosureAuditParentDto(BaseModel):
    control:str
    service: str
    operation: str
    id_user: str
    response: str
    date: str