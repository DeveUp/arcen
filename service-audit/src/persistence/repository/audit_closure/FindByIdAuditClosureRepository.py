from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB

from src.util.constant import DATABASE

class FindByIdAuditClosureRepository(IRepository):

    def __init__(self, table_id:str):
        self.db = AuditDB()
        self.collection = self.db.get_db_audit_id(table_id)

    def execute(self, data:dict):
        id = data[DATABASE['table']['audit_closure']['column'][0]]
        key = DATABASE['table']['audit_closure']['name']+"."+DATABASE['table']['audit_closure']['column'][0]
        return self.collection.find_one({
            key: id
        })
       