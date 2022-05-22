from pymongo import MongoClient

from src.util.constant import DATABASE_MONGODB, DATABASE_MONGODB_NAME_TABLE, DATABASE_MONGODB_NAME, COLUMN_CONTROL_AUDIT_NAME

class AuditDB:

    def get_db(self, db:str, table):
        client = MongoClient(db)
        database_audit = client[DATABASE_MONGODB_NAME]
        return database_audit[table]

    def get_db_audit(self):
        return self.get_db(DATABASE_MONGODB, DATABASE_MONGODB_NAME_TABLE)

    def get_db_control_audit(self):
        return self.get_db(DATABASE_MONGODB, COLUMN_CONTROL_AUDIT_NAME)
    
    def get_db_audit_id(self, id:str):
        table = DATABASE_MONGODB_NAME_TABLE+id
        return self.get_db(DATABASE_MONGODB, table)