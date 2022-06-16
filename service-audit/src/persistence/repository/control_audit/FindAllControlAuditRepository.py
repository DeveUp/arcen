from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB

class FindAllControlAuditRepository(IRepository):

    def __init__(self):
        self.db = AuditDB()
        self.collection = self.db.get_db_control_audit()

    def execute(self, data:dict):
        return self.collection.find()