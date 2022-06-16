from src.service.IService import IService

from src.persistence.repository.audit.FindByIdAuditRepository import FindByIdAuditRepository
from src.persistence.schema.AuditSchema import AuditSchema

from src.util.constant import RESPONSE
from src.util.common import get_exception_http

# @Class FindByIdAuditService - Servicio de auditoria
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class FindByIdAuditService(IService):

    # @Method - Contructor 
    # @Return - Void
    def __init__(self):
        self.repository = FindByIdAuditRepository()
        self.schema = AuditSchema()

    # @Override
    # @Method - Consulta una auditoria por su pk
    # @Parameter - data - Json con el pk de la auditoria
    # @Return - Audit
    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.entity(element)
        except:
            element = None
        finally:
            if element == None:
                raise get_exception_http(RESPONSE['audit']['get']['find_by_id']['error']['default'])
            return element