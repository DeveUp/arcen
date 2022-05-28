from pydantic import BaseModel

from src.model.entity.Audit import Audit

class ClosureAuditRequest(BaseModel):
    control: str
    audit: Audit
    date_start: str
    date_end: str