from src.persistence.repository.IRepository import IRepository

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB
from src.persistence.schema.AuditSchema import AuditSchema

class FindAllAuditRepository(IRepository):

    def __init__(self):
        self.db = AuditDB()
        self.schema = AuditSchema()
        self.collection = self.db.get_db_audit()

    def execute(self, data):
        try:
            elements = self.collection.find()
            elements = self.schema.audits(elements)
        except:
            elements= None
        return elements