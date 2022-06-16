from src.service.IService import IService

from src.persistence.repository.audit_closure.FindByIdAuditClosureRepository import FindByIdAuditClosureRepository
from src.persistence.schema.AuditClosureSchema import AuditClosureSchema

from src.util.constant import RESPONSE
from src.util.common import get_exception_http

# @Class FindByIdAuditClosureService - Servicio de cierre auditoria
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class FindByIdAuditClosureService(IService):

    # @Method - Contructor 
    # @Parameter - table_id - Representa el pk de la tabla de cierre
    # @Return - Void
    def __init__(self, table_id: str):
        self.repository = FindByIdAuditClosureRepository(table_id)
        self.schema = AuditClosureSchema()

    # @Override
    # @Method - Consulta un cierre de auditoria por su pk
    # @Parameter - data - Json con el pk de la auditoria
    # @Return - AuditClosure
    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.entity(element)
        except:
            element = None
        finally:
            if element == None:
                raise get_exception_http(RESPONSE['audit_closure']['get']['find_by_id']['error']['default'])
            return element