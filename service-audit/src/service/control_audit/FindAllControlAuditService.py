from src.service.IService import IService

from src.persistence.repository.control_audit.FindAllControlAuditRepository import FindAllControlAuditRepository
from src.persistence.schema.ControlAuditSchema import ControlAuditSchema

# @Class FindAllControlAuditService - Servicio de control auditoria
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class FindAllControlAuditService(IService):

    # @Method - Contructor 
    # @Return - Void
    def __init__(self):
        self.repository = FindAllControlAuditRepository()
        self.schema = ControlAuditSchema()

    # @Override
    # @Method - Consulta todos los controles de auditoria
    # @Parameter - data - No aplica
    # @Return - list
    def execute(self, data:dict):
        elements = self.repository.execute(data)
        return self.schema.list(elements)