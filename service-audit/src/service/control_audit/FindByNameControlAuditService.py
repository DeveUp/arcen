from src.service.IService import IService

from src.persistence.repository.control_audit.FindByNameControlAuditRepository import FindByNameControlAuditRepository
from src.persistence.schema.ControlAuditSchema import ControlAuditSchema

from src.util.constant import RESPONSE
from src.util.common import get_exception_http

# @Class FindByNameControlAuditService - Servicio de control auditoria
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class FindByNameControlAuditService(IService):

    # @Method - Contructor 
    # @Return - Void
    def __init__(self):
        self.repository = FindByNameControlAuditRepository()
        self.schema = ControlAuditSchema()

    # @Override
    # @Method - Consulta un control de auditoria por su nombre
    # @Parameter - data - Json con el nombre del cierre de auditoria
    # @Return - ControlAudit
    def execute(self, data:dict):
        try:
          element = self.repository.execute(data)
          element = self.schema.entity(element)
        except:
            element = None
        if element == None:
            raise get_exception_http(RESPONSE['control_audit']['get']['find_by_name']['error']['default'])
        return  element