from pydantic import BaseModel

# @Class ControlAuditRequest - Peticion de control auditoria
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class ControlAuditRequest(BaseModel):
    name: str
    date_start: str
    date_end: str
    date:str