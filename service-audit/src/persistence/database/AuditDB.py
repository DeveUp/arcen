from pymongo import MongoClient

from src.util.constant import DATABASE_MONGODB, DATABASE_MONGODB_NAME_TABLE

class AuditDB:

    def get_db(self, db:str, table):
        client = MongoClient(db)
        database_audit = client.arcen_audit
        return database_audit[table]

    def get_db_audit(self):
        return self.get_db(DATABASE_MONGODB, DATABASE_MONGODB_NAME_TABLE)