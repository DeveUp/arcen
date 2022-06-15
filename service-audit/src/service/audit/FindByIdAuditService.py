from src.service.IService import IService

from src.persistence.repository.audit.FindByIdAuditRepository import FindByIdAuditRepository
from src.persistence.schema.AuditSchema import AuditSchema

from src.util.constant import RESPONSE
from src.util.common import get_exception_http

class FindByIdAuditService(IService):

    def __init__(self):
        self.repository = FindByIdAuditRepository()
        self.schema = AuditSchema()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            return self.schema.entity(element)
        except:
            raise get_exception_http(RESPONSE['audit']['get']['find_by_id']['error']['default'])