from pydantic import BaseModel

# @Class AuditDto - Dto de auditoria
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class AuditDto(BaseModel):
    service: str
    operation: str
    id_user: str
    response: str