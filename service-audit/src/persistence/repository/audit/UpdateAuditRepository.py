from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB
from src.persistence.schema.AuditSchema import AuditSchema

class UpdateAuditRepository(IRepository):

    def __init__(self):
        self.db = AuditDB()
        self.schema = AuditSchema()
        self.collection = self.db.get_db_audit()

    def execute(self, data:dict):
        try:
            id = data['id']
            audit = data['audit']
        except:
            return None
        try:
            id = self.collection.find_one_and_update({
                "_id": ObjectId(id)
            },{
                "$set": dict(audit)
            })
            audit = self.findAuditById.execute(id)
        except:
            audit= None
        return audit