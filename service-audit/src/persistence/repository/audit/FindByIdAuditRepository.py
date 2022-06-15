from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB

from src.util.constant import DATABASE

class FindByIdAuditRepository(IRepository):

    def __init__(self):
        self.db = AuditDB()
        self.collection = self.db.get_db_audit()
        self.data = DATABASE['table']['audit']

    def execute(self, data:dict):
        id = ObjectId(data[self.data['column']['id']])
        return self.collection.find_one({self.data['pk']:id})
       