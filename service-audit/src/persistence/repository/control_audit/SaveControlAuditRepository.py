from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB

from src.util.constant import DATABASE

class SaveControlAuditRepository(IRepository):

    def __init__(self):
        self.db = AuditDB()
        self.collection = self.db.get_db_control_audit()

    def execute(self, data:dict):
        control_audit = dict(data[DATABASE['table']['name']])
        id = self.collection.insert_one(control_audit)
        return id.inserted_id