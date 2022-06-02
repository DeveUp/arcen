from src.feign.Feign import Feign
from src.model.dto.AuditDto import AuditDto
from src.util.constant import FEIGN_ENDPOINT_AUDIT, FEIGN_ENDPOINT_AUDIT_SAVE
from src.util.constant import RESPONSE_STATUS_CODE_AUDIT_ERROR_SAVE, RESPONSE_MSG_AUDIT_ERROR_SAVE

class AuditFeign:

    def __init__(self):
        self.feign = Feign(FEIGN_ENDPOINT_AUDIT)
        
    def build(self, service:str, operation:str, response:str):
        return { 
            "service": "BLOCK",
            "operation": "DELETE_BY_ID",
            "id_user": "SYSTEM",
            "response": "TEST"
        }
    
    def save(self, data):
        return self.feign.post(FEIGN_ENDPOINT_AUDIT_SAVE, data, RESPONSE_STATUS_CODE_AUDIT_ERROR_SAVE, RESPONSE_MSG_AUDIT_ERROR_SAVE)
