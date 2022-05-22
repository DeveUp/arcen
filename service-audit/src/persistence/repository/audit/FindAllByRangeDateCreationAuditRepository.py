from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB
from src.util.constant import COLUMN_AUDIT_DATE_NAME
from src.util.constant import COLUMN_AUDIT_DATE_START_NAME, COLUMN_AUDIT_DATE_END_NAME

class FindAllByRangeDateCreationAuditRepository(IRepository):

    def __init__(self):
        self.db = AuditDB()
        self.collection = self.db.get_db_audit()

    def execute(self, data:dict):
        date_start = data[COLUMN_AUDIT_DATE_START_NAME]
        date_end = data[COLUMN_AUDIT_DATE_END_NAME]
        return self.collection.find({
            COLUMN_AUDIT_DATE_NAME:{
                "$gte": date_start, 
                "$lt": date_end
            }
        })