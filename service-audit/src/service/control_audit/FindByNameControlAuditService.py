from src.service.IService import IService
from src.persistence.repository.control_audit.FindByNameControlAuditRepository import FindByNameControlAuditRepository
from src.persistence.schema.ControlAuditSchema import ControlAuditSchema
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_NAME_NOT_CONTENT, RESPONSE_MSG_CONTROL_AUDIT_FIND_BY_NAME_NOT_CONTENT
from src.util.common import get_exception_http_build

class FindByNameControlAuditService(IService):

    def __init__(self):
        self.repository = FindByNameControlAuditRepository()
        self.schema = ControlAuditSchema()

    def execute(self, data:dict):
        try:
          element = self.repository.execute(data)
          element = self.schema.entity(element)
        except:
            raise get_exception_http_build(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_NAME_NOT_CONTENT, RESPONSE_MSG_CONTROL_AUDIT_FIND_BY_NAME_NOT_CONTENT)
        if element == None:
            raise get_exception_http_build(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_NAME_NOT_CONTENT, RESPONSE_MSG_CONTROL_AUDIT_FIND_BY_NAME_NOT_CONTENT)
        return  element