from pydantic import BaseModel

from src.model.entity.Audit import Audit

class ClosureAudit(BaseModel):
    id: str
    control: str
    audit: Audit
    date: str
