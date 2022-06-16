from src.service.IService import IService

from src.persistence.repository.audit_closure.FindAllAuditClosureRepository import FindAllAuditClosureRepository
from src.persistence.schema.AuditClosureSchema import AuditClosureSchema

# @Class FindAllAuditClosureService - Servicio de cierre auditoria
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class FindAllAuditClosureService(IService):

    # @Method - Contructor 
    # @Parameter - table_id - Representa el pk de la tabla de cierre
    # @Return - Void
    def __init__(self, table_id: str):
        self.repository = FindAllAuditClosureRepository(table_id)
        self.schema = AuditClosureSchema()

    # @Override
    # @Method - Consulta todos los cierres de auditoria
    # @Parameter - data - No aplica
    # @Return - list
    def execute(self, data:dict):
        elements = self.repository.execute(data)
        return self.schema.list(elements)