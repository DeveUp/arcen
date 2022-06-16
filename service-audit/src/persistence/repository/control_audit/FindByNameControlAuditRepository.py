from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB

from src.util.constant import DATABASE

class FindByNameControlAuditRepository(IRepository):

    def __init__(self):
        self.db = AuditDB()
        self.collection = self.db.get_db_control_audit()

    def execute(self, data:dict):
        self.name = DATABASE['table']['control_audit']['column'][1]
        return self.collection.find_one({
            self.name:data[self.name]
        })