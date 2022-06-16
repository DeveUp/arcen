from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB

from src.util.constant import DATABASE

class SaveAuditRepository(IRepository):

    def __init__(self):
        self.db = AuditDB()
        self.collection = self.db.get_db_audit()

    def execute(self, data:dict):
        audit = dict(data[DATABASE['table']['audit']['name']])
        id = self.collection.insert_one(audit)
        return id.inserted_id