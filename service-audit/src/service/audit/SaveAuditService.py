from src.service.IService import IService
from src.persistence.repository.audit.SaveAuditRepository import SaveAuditRepository
from src.persistence.schema.AuditSchema import AuditSchema
from src.service.audit.FindByIdAuditService import FindByIdAuditService
from src.util.constant import COLUMN_AUDIT, COLUMN_AUDIT_ID_TWO
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_AUDIT_SAVE_ERROR_SAVE
from src.util.common import generate_date, get_ip_address, get_http_exception

class SaveAuditService(IService):

    def __init__(self):
        self.repository = SaveAuditRepository()
        self.findByIdAudit = FindByIdAuditService()
        self.schema = AuditSchema()

    def execute(self, data:dict):
        try:
            audit = self.schema.dict(dict(data[COLUMN_AUDIT]), generate_date(), get_ip_address())
            data = dict({COLUMN_AUDIT: self.schema.request(dict(audit))})
            element = self.repository.execute(data)
        except:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_AUDIT_SAVE_ERROR_SAVE)
        # Find audit by id
        data = dict({COLUMN_AUDIT_ID_TWO: element})
        return self.findByIdAudit.execute(data)