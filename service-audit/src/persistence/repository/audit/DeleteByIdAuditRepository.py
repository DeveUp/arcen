from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB
from src.persistence.schema.AuditSchema import AuditSchema

class DeleteByIdAuditRepository(IRepository):

    def __init__(self):
        self.db = AuditDB()
        self.schema = AuditSchema()
        self.collection = self.db.get_db_audit()

    def execute(self, data):
        try:
            id = ObjectId(data['id'])
            element = self.collection.find_one_and_delete({"_id":id})
            element = True
        except:
            element= None
        return element