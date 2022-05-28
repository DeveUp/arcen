from src.service.IService import IService
from src.persistence.repository.audit.FindByIdAuditRepository import FindByIdAuditRepository
from src.persistence.schema.AuditSchema import AuditSchema
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_AUDIT_FIND_BY_ID_NOT_CONTENT
from src.util.common import get_http_exception

class FindByIdAuditService(IService):

    def __init__(self):
        self.repository = FindByIdAuditRepository()
        self.schema = AuditSchema()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.entity(element)
        except:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_AUDIT_FIND_BY_ID_NOT_CONTENT)
        return element