from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB
from src.util.constant import COLUMN_CONTROL_AUDIT_ID, COLUMN_CONTROL_AUDIT_ID_TWO

class FindByIdControlAuditRepository(IRepository):

    def __init__(self):
        self.db = AuditDB()
        self.collection = self.db.get_db_control_audit()

    def execute(self, data:dict):
        id = ObjectId(data[COLUMN_CONTROL_AUDIT_ID_TWO])
        return self.collection.find_one({COLUMN_CONTROL_AUDIT_ID:id})
       