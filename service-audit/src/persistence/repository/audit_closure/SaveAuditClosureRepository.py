from src.persistence.repository.IRepository import IRepository
from src.persistence.repository.audit.FindByIdAuditRepository import FindByIdAuditRepository
from src.persistence.database.AuditDB import AuditDB
from src.util.constant import COLUMN_AUDIT_NAME, COLUMN_AUDIT_ID_TWO_NAME

class SaveAuditClosureRepository(IRepository):

    def __init__(self):
        self.db = AuditDB()
        self.find_by_id = FindByIdAuditRepository()
        self.collection = self.db.get_db_audit()

    def execute(self, data:dict):
        try:
            audit = dict(data[COLUMN_AUDIT_NAME])
            id = self.collection.insert_one(audit)
            data = dict({COLUMN_AUDIT_ID_TWO_NAME: id.inserted_id})
            audit = self.find_by_id.execute(data)
        except:
            audit= None
        return audit