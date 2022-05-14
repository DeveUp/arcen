from src.persistence.repository.IRepository import IRepository
from src.persistence.repository.audit.FindByIdAuditRepository import FindByIdAuditRepository
from src.persistence.database.AuditDB import AuditDB

class SaveAuditRepository(IRepository):

    def execute(data):
        db = AuditDB()
        collection = db.get_db_audit()
        id = collection.insert_one(dict(data.audit))
        find = FindByIdAuditRepository()
        return find.execute(id)