from src.persistence.repository.IRepository import IRepository
from src.persistence.repository.control_audit.FindByIdControlAuditRepository import FindByIdControlAuditRepository
from src.persistence.database.AuditDB import AuditDB
from src.util.constant import COLUMN_CONTROL_AUDIT_NAME, COLUMN_CONTROL_AUDIT_ID_TWO_NAME

class SaveControlAuditRepository(IRepository):

    def __init__(self):
        self.db = AuditDB()
        self.find_by_id = FindByIdControlAuditRepository()
        self.collection = self.db.get_db_control_audit()

    def execute(self, data:dict):
        try:
            control_audit = dict(data[COLUMN_CONTROL_AUDIT_NAME])
            id = self.collection.insert_one(control_audit)
            data = dict({COLUMN_CONTROL_AUDIT_ID_TWO_NAME: id.inserted_id})
            control_audit = self.find_by_id.execute(data)
        except:
            control_audit= None
        return control_audit