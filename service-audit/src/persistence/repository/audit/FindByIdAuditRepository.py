from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB
from src.persistence.schema.AuditSchema import AuditSchema

class FindByIdAuditRepository(IRepository):

    def __init__(self):
        self.db = AuditDB()
        self.schema = AuditSchema()
        self.collection = self.db.get_db_audit()

    def execute(self, data):
        try:
            id = ObjectId(data['id'])
            element = self.collection.find_one({"_id":id})
            element = self.schema.audit(element)
        except:
            element= None
        return element