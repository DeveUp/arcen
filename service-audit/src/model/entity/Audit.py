from pydantic import BaseModel

# @Class Audit - Entidad de auditoria
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class Audit(BaseModel):
    id:str
    service:str
    operation:str
    id_user:str
    ip_address:str
    response:str
    date:str