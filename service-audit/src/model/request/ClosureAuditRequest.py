from pydantic import BaseModel

# @Class ClosureAuditRequest - Peticion de cierre auditoria
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class ClosureAuditRequest(BaseModel):
    control: str
    audit: dict
    date:str
