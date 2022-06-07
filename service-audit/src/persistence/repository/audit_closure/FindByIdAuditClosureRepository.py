from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB
from src.util.constant import COLUMN_AUDIT_CLOSURE_ID_TWO, COLUMN_AUDIT

class FindByIdAuditClosureRepository(IRepository):

    def __init__(self, table_id:str):
        self.db = AuditDB()
        self.collection = self.db.get_db_audit_id(table_id)

    def execute(self, data:dict):
        id = data[COLUMN_AUDIT_CLOSURE_ID_TWO]
        key = COLUMN_AUDIT+"."+COLUMN_AUDIT_CLOSURE_ID_TWO
        return self.collection.find_one({
            key: id
        })
       