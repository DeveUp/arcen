from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB
from src.util.constant import COLUMN_AUDIT_NAME, COLUMN_AUDIT_ID_NAME, COLUMN_AUDIT_ID_TWO_NAME

class UpdateAuditRepository(IRepository):

    def __init__(self):
        self.db = AuditDB()
        self.collection = self.db.get_db_audit()

    def execute(self, data:dict):
        id = data[COLUMN_AUDIT_ID_TWO_NAME]
        audit = data[COLUMN_AUDIT_NAME]
        id = self.collection.find_one_and_update({
            COLUMN_AUDIT_ID_NAME: ObjectId(id)
        },{
            "$set": dict(audit)
        })
        return self.findAuditById.execute(id)