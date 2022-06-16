from pydantic import BaseModel

# @Class ControlAuditDto - Dto de control auditoria
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class ControlAuditDto(BaseModel):
    name: str
    date_start: str
    date_end: str