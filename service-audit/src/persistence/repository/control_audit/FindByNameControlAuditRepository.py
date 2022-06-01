from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB
from src.util.constant import COLUMN_CONTROL_AUDIT_NAME

class FindByNameControlAuditRepository(IRepository):

    def __init__(self):
        self.db = AuditDB()
        self.collection = self.db.get_db_control_audit()

    def execute(self, data:dict):
        return self.collection.find_one({
            COLUMN_CONTROL_AUDIT_NAME:data[COLUMN_CONTROL_AUDIT_NAME]
        })