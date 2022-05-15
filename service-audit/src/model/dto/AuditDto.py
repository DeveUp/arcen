from pydantic import BaseModel

class AuditDto(BaseModel):
    service: str
    operation: str
    id_user: str
    response: str
    date: str