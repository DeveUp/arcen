from pydantic import BaseModel

from src.model.entity.Audit import Audit

# @Class ClosureAudit - Entidad de cierre auditoria
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class ClosureAudit(BaseModel):
    id: str
    control: str
    audit: Audit
    date: str
