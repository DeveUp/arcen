from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB
from src.util.constant import COLUMN_AUDIT_ID, COLUMN_AUDIT_ID_TWO

class FindByIdAuditClosureRepository(IRepository):

    def __init__(self, table_id:str):
        self.db = AuditDB()
        self.collection = self.db.get_db_audit_id(table_id)

    def execute(self, data:dict):
        id = ObjectId(data[COLUMN_AUDIT_ID_TWO])
        return self.collection.find_one({COLUMN_AUDIT_ID:id})
       