from datetime import datetime

from src.service.IService import IService
from src.persistence.repository.control_audit.SaveControlAuditRepository import SaveControlAuditRepository
from src.persistence.schema.ControlAuditSchema import ControlAuditSchema
from src.util.constant import COLUMN_CONTROL_AUDIT_NAME, FORMAT_DATE

class SaveControlAuditClosureService(IService):

    def __init__(self):
        self.repository = SaveControlAuditRepository()
        self.schema = ControlAuditSchema()

    def execute(self, data:dict):
        try:
            date = str(datetime.today().strftime(FORMAT_DATE))
            control_audit = self.schema.dict(dict(data[COLUMN_CONTROL_AUDIT_NAME]), date)
            control_audit = self.schema.dto(dict(control_audit))
            data = dict({COLUMN_CONTROL_AUDIT_NAME: control_audit})
            element = self.schema.entity(self.repository.execute(data))
        except:
            element= None
        return element