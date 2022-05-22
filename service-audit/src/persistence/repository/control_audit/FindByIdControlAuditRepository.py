from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB
from src.util.constant import COLUMN_AUDIT_ID_NAME, COLUMN_AUDIT_ID_TWO_NAME

class FindByIdControlAuditRepository(IRepository):

    def __init__(self):
        self.db = AuditDB()
        self.collection = self.db.get_db_control_audit()

    def execute(self, data:dict):
        id = ObjectId(data[COLUMN_AUDIT_ID_TWO_NAME])
        return self.collection.find_one({COLUMN_AUDIT_ID_NAME:id})
       