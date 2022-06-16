from pydantic import BaseModel

# @Class AuditRequest - Peticion de auditoria
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class AuditRequest(BaseModel):
    service:str
    operation:str
    id_user:str
    ip_address:str
    response:str
    date:str