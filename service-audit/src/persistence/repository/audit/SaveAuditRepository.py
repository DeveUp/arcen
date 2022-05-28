from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB
from src.util.constant import COLUMN_AUDIT_NAME

class SaveAuditRepository(IRepository):

    def __init__(self):
        self.db = AuditDB()
        self.collection = self.db.get_db_audit()

    def execute(self, data:dict):
        audit = dict(data[COLUMN_AUDIT_NAME])
        id = self.collection.insert_one(audit)
        return id.inserted_id