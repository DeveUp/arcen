from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB

from src.util.constant import DATABASE

class FindByIdControlAuditRepository(IRepository):

    def __init__(self):
        self.db = AuditDB()
        self.collection = self.db.get_db_control_audit()

    def execute(self, data:dict):
        self.id = DATABASE['table']['control_audit']['column'][0]
        id = ObjectId(data[self.id])
        return self.collection.find_one({
            self.id:id
        })
       