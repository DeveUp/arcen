from src.service.IService import IService

from src.persistence.repository.control_audit.FindByIdControlAuditRepository import FindByIdControlAuditRepository
from src.persistence.schema.ControlAuditSchema import ControlAuditSchema

from src.util.constant import RESPONSE
from src.util.common import get_exception_http

# @Class FindByIdControlAuditService - Servicio de control auditoria
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class FindByIdControlAuditService(IService):

    # @Method - Contructor 
    # @Return - Void
    def __init__(self):
        self.repository = FindByIdControlAuditRepository()
        self.schema = ControlAuditSchema()

    # @Override
    # @Method - Consulta un control de auditoria por su pk
    # @Parameter - data - Json con el pk del control de auditoria
    # @Return - ControlAudit
    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.entity(element)
        except:
            element = None
        finally:
            if element == None:
                raise get_exception_http(RESPONSE['control_audit']['get']['find_by_id']['error']['default'])
        return element