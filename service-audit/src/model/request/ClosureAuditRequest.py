from pydantic import BaseModel

from src.model.entity.Audit import Audit

class ClosureAuditRequest(BaseModel):
    control: str
    audit: dict
    date:str
