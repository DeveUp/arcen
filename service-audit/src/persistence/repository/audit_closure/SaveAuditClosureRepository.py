from src.persistence.repository.IRepository import IRepository
from src.persistence.repository.control_audit.FindByIdControlAuditRepository import FindByIdControlAuditRepository
from src.persistence.database.AuditDB import AuditDB
from src.util.constant import COLUMN_AUDIT_CLOSURE

class SaveAuditClosureRepository(IRepository):

    def __init__(self, table_id: str):
        self.db = AuditDB()
        self.collection = self.db.get_db_audit_id(table_id)

    def execute(self, data:dict):
        closure_audit = dict(data[COLUMN_AUDIT_CLOSURE])
        id = self.collection.insert_one(closure_audit)
        return id.inserted_id