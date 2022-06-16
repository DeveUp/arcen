from src.service.IService import IService
from src.persistence.repository.control_audit.FindByIdControlAuditRepository import FindByIdControlAuditRepository
from src.persistence.schema.ControlAuditSchema import ControlAuditSchema
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_CONTROL_AUDIT_FIND_BY_ID_NOT_CONTENT
from src.util.common import get_exception_http_build

class FindByIdControlAuditService(IService):

    def __init__(self):
        self.repository = FindByIdControlAuditRepository()
        self.schema = ControlAuditSchema()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            return self.schema.entity(element)
        except:
            raise get_exception_http_build(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_CONTROL_AUDIT_FIND_BY_ID_NOT_CONTENT)