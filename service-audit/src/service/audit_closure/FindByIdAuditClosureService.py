from src.service.IService import IService

from src.persistence.repository.audit_closure.FindByIdAuditClosureRepository import FindByIdAuditClosureRepository
from src.persistence.schema.AuditClosureSchema import AuditClosureSchema

from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_CLOSURE_AUDIT_FIND_BY_ID_NOT_CONTENT
from src.util.common import get_exception_http_build

class FindByIdAuditClosureService(IService):

    def __init__(self, table_id: str):
        self.repository = FindByIdAuditClosureRepository(table_id)
        self.schema = AuditClosureSchema()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data) 
        except:
            raise get_exception_http_build(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_CLOSURE_AUDIT_FIND_BY_ID_NOT_CONTENT)
        if element == None:
            raise get_exception_http_build(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_CLOSURE_AUDIT_FIND_BY_ID_NOT_CONTENT)
        return self.schema.entity(element)