"""
    @description - Feign Audit - Comunicacion el microservicio auditoria servicio auditoria.
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-18
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from src.feign.Feign import Feign

from src.model.dto.AuditDto import AuditDto

from src.util.constant import FEIGN
from src.util.common import find_env

class AuditFeign:

    # @method - Contructor 
    # @return - Void
    def __init__(self, name):
        self.endpoint = find_env(name)
        self.feign = Feign(self.endpoint)
        self.system = "SYSTEM"

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
                id_user= self.system,
                response= response
            )
        )
    
    # @method - Consume la operacion registrar microservicio auditoria
    # @parameter - data - Json de la peticion del servicio
    # @return - Json 
    def save(self, operation, data):
        self.operation = operation
        return self.feign.post(self.operation, data, FEIGN['microservice']['audit']['service']['audit']['response']['error']['default'])
