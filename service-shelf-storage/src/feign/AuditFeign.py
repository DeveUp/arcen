"""
    @name - AuditFeign
    @description - Comunicacion con el microservicio auditoria servicio auditoria.
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from src.feign.Feign import Feign
from src.model.dto.AuditDto import AuditDto
from src.util.constant import FEIGN_ENDPOINT_AUDIT, FEIGN_ENDPOINT_AUDIT_SAVE
from src.util.constant import RESPONSE_STATUS_CODE_AUDIT_ERROR_SAVE, RESPONSE_MSG_AUDIT_ERROR_SAVE

class AuditFeign:

    # @method - Contructor 
    # @return - Void
    def __init__(self):
        self.feign = Feign(FEIGN_ENDPOINT_AUDIT)

    # @method - Construye la peticion al servicio
    # @parameter - service - Representa servicio
    # @parameter - operation - Representa la operacion
    # @parameter - response - Representa la respuesta
    # @return - Json     
    def build(self, service:str, operation:str, response:str) -> dict:
        return dict(
            AuditDto(
                service= service,
                operation= operation,
                id_user= "system",
                response= response
            )
        )
    
    # @method - Consume la operacion registrar microservicio auditoria
    # @parameter - data - Json de la peticion del servicio
    # @return - Json 
    def save(self, data):
        return self.feign.post(FEIGN_ENDPOINT_AUDIT_SAVE, data, RESPONSE_STATUS_CODE_AUDIT_ERROR_SAVE, RESPONSE_MSG_AUDIT_ERROR_SAVE)