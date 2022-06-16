from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB

class FindAllAuditClosureRepository(IRepository):

    def __init__(self, table_id:str):
        self.db = AuditDB()
        self.collection = self.db.get_db_audit_id(table_id)

    def execute(self, data:dict):
        return self.collection.find()