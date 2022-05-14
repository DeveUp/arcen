from src.persistence.repository.IRepository import IRepository
from src.persistence.repository.audit.FindByIdAuditRepository import FindByIdAuditRepository
from src.persistence.database.AuditDB import AuditDB
from src.persistence.schema.AuditSchema import AuditSchema

class SaveAuditRepository(IRepository):

    def __init__(self):
        self.db = AuditDB()
        self.schema = AuditSchema()
        self.collection = self.db.get_db_audit()
        self.findAuditById = FindByIdAuditRepository()

    def execute(self, data):
        try:
            audit = dict(data['audit'])
            id = self.collection.insert_one(audit)
            id = dict({'id': id.inserted_id})
            audit = self.findAuditById.execute(id)
        except:
            audit= None
        return audit