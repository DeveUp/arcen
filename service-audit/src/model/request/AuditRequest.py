from ipaddress import ip_address
from pydantic import BaseModel

class AuditRequest(BaseModel):
    service:str
    operation:str
    id_user:str
    ip_address:str
    response:str
    date:str