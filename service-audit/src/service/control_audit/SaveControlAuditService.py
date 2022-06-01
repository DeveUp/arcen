from src.service.IService import IService
from src.persistence.repository.control_audit.SaveControlAuditRepository import SaveControlAuditRepository
from src.persistence.schema.ControlAuditSchema import ControlAuditSchema
from src.service.control_audit.FindByNameControlAuditService import FindByNameControlAuditService
from src.service.control_audit.FindByIdControlAuditService import FindByIdControlAuditService
from src.util.constant import COLUMN_CONTROL_AUDIT_NAME, COLUMN_CONTROL_AUDIT_ID_TWO
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_CONTROL_AUDIT_SAVE_ERROR_SAVE
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_NAME_SAVE, RESPONSE_MSG_CONTROL_AUDIT_SAVE_ERROR_NAME_SAVE, COLUMN_CONTROL_AUDIT_NAME_NAME
from src.util.common import generate_date, get_http_exception

class SaveControlAuditClosureService(IService):

    def __init__(self):
        self.repository = SaveControlAuditRepository()
        self.findByIdControlAudit = FindByIdControlAuditService()
        self.findByNameControlAudit = FindByNameControlAuditService()
        self.schema = ControlAuditSchema()

    def execute(self, data:dict):
        data = data[COLUMN_CONTROL_AUDIT_NAME]
        # Validate find by name control audit
        isErrorName = True
        try:
            control_audit = self.findByNameControlAudit.execute(
                dict({
                    COLUMN_CONTROL_AUDIT_NAME_NAME: data.name
                })
            )
        except:
            isErrorName = False
        if isErrorName:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_NAME_SAVE, RESPONSE_MSG_CONTROL_AUDIT_SAVE_ERROR_NAME_SAVE)
        # Save control audit
        try:
            control_audit = self.schema.dict(dict(data), generate_date())
            data = dict({COLUMN_CONTROL_AUDIT_NAME: self.schema.request(dict(control_audit))})
            element = self.repository.execute(data)
        except:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_CONTROL_AUDIT_SAVE_ERROR_SAVE)
        # Find control audit by id
        data = dict({COLUMN_CONTROL_AUDIT_ID_TWO: element})
        return self.findByIdControlAudit.execute(data)