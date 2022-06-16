from src.service.IService import IService

from src.persistence.repository.audit.FindAllAuditRepository import FindAllAuditRepository
from src.persistence.schema.AuditSchema import AuditSchema

# @Class FindAllAuditService - Servicio de auditoria
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class FindAllAuditService(IService):

    # @Method - Contructor 
    # @Return - Void
    def __init__(self):
        self.repository = FindAllAuditRepository()
        self.schema = AuditSchema()

    # @Override
    # @Method - Consulta todas las auditorias
    # @Parameter - data - No aplica
    # @Return - list
    def execute(self, data:dict):
        elements = self.repository.execute(data)
        return self.schema.list(elements)