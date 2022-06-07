from src.persistence.repository.IRepository import IRepository
from src.persistence.repository.control_audit.FindByIdControlAuditRepository import FindByIdControlAuditRepository
from src.persistence.database.AuditDB import AuditDB
from src.util.constant import COLUMN_CONTROL_AUDIT

class SaveControlAuditRepository(IRepository):

    def __init__(self):
        self.db = AuditDB()
        self.find_by_id = FindByIdControlAuditRepository()
        self.collection = self.db.get_db_control_audit()

    def execute(self, data:dict):
        control_audit = dict(data[COLUMN_CONTROL_AUDIT])
        id = self.collection.insert_one(control_audit)
        return id.inserted_id