from src.service.IService import IService
from src.persistence.repository.control_audit.SaveControlAuditRepository import SaveControlAuditRepository
from src.persistence.schema.ControlAuditSchema import ControlAuditSchema
from src.service.control_audit.FindByIdControlAuditService import FindByIdControlAuditService
from src.util.constant import COLUMN_CONTROL_AUDIT_NAME, COLUMN_CONTROL_AUDIT_ID_TWO_NAME
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_CONTROL_AUDIT_SAVE_ERROR_SAVE
from src.util.common import generate_date, get_http_exception

class SaveControlAuditClosureService(IService):

    def __init__(self):
        self.repository = SaveControlAuditRepository()
        self.findByIdControlAudit = FindByIdControlAuditService()
        self.schema = ControlAuditSchema()

    def execute(self, data:dict):
        try:
            control_audit = self.schema.dict(dict(data[COLUMN_CONTROL_AUDIT_NAME]), generate_date())
            data = dict({COLUMN_CONTROL_AUDIT_NAME: self.schema.request(dict(control_audit))})
            element = self.repository.execute(data)
        except:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_CONTROL_AUDIT_SAVE_ERROR_SAVE)
        # Find control audit by id
        data = dict({COLUMN_CONTROL_AUDIT_ID_TWO_NAME: element})
        return self.findByIdControlAudit.execute(data)