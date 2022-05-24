from datetime import datetime

from src.service.IService import IService
from src.persistence.repository.audit.SaveAuditRepository import SaveAuditRepository
from src.persistence.schema.AuditSchema import AuditSchema
from src.util.constant import COLUMN_AUDIT_NAME, FORMAT_DATE

class SaveAuditService(IService):

    def __init__(self):
        self.repository = SaveAuditRepository()
        self.schema = AuditSchema()

    def execute(self, data:dict):
        try:
            date = str(datetime.today().strftime(FORMAT_DATE))
            audit = self.schema.audit_dict(dict(data[COLUMN_AUDIT_NAME]), date)
            audit = self.schema.audit_dto(dict(audit))
            data = dict({COLUMN_AUDIT_NAME: audit})
            element = self.schema.audit(self.repository.execute(data))
        except:
            element= None
        return element