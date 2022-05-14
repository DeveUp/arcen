from bson import ObjectId

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB
from src.persistence.schema.AuditSchema import AuditSchema

class FindByIdAuditRepository(IRepository):

    def execute(data):
        db = AuditDB()
        schema = AuditSchema()
        collection = db.get_db_audit()
        return schema.audit_dic(collection.find_one({"_id": ObjectId(data.id)}))