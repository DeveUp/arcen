from pydantic import BaseModel

# @Class ControlAudit - Entidad de control auditoria
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class ControlAudit(BaseModel):
    id:str
    name: str
    date_start: str
    date_end: str
    date:str