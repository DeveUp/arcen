from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB

from src.util.constant import DATABASE

class FindAllByRangeDateCreationAuditRepository(IRepository):

    def __init__(self):
        self.db = AuditDB()
        self.collection = self.db.get_db_audit()

    def execute(self, data:dict):
        date = DATABASE['table']['audit']['column'][6]
        length = len(DATABASE['table']['audit']['column']) - 1;
        date_start = DATABASE['table']['audit']['column'][length][0]
        date_end = DATABASE['table']['audit']['column'][length][1]
        return self.collection.find({
            date:{
                "$gte": date_start, 
                "$lt": date_end
            }
        })