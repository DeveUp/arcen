from src.service.IService import IService
from src.persistence.repository.audit_closure.FindByIdAuditClosureRepository import FindByIdAuditClosureRepository
from src.persistence.schema.AuditSchema import AuditSchema
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_CLOSURE_AUDIT_FIND_BY_ID_NOT_CONTENT
from src.util.common import get_http_exception

class FindByIdAuditClosureService(IService):

    def __init__(self, table_id: str):
        self.repository = FindByIdAuditClosureRepository(table_id)
        self.schema = AuditSchema()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            return self.schema.entity(element)
        except:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_CLOSURE_AUDIT_FIND_BY_ID_NOT_CONTENT)