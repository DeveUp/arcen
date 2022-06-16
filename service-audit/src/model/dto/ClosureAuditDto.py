from pydantic import BaseModel

# @Class ClosureAuditDto - Dto de cierre auditoria
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class ClosureAuditDto(BaseModel):
    id: str
    date_start: str
    date_end: str